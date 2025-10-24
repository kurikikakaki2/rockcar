from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from urllib.parse import quote_plus

import requests

from models.schemas import RespuestaCategorias, Vehiculo
from scraper.parser import extract_categories
from scraper.session import session_scope

BASE_CATALOG_URL = "https://www.rockauto.com/es/catalog"


@dataclass(slots=True)
class CatalogRequest:
    vehiculo: Vehiculo

    def to_url(self) -> str:
        marca = quote_plus(self.vehiculo.marca.lower())
        modelo = quote_plus(self.vehiculo.modelo.lower())
        motor = quote_plus(self.vehiculo.motor.lower())
        return \
            f"{BASE_CATALOG_URL}/{marca},{self.vehiculo.anio},{modelo},{motor},{self.vehiculo.id}"


class CatalogScraperError(RuntimeError):
    """Error raised when the catalog cannot be retrieved."""


def get_categories(vehiculo: Vehiculo, headers: Optional[dict[str, str]] = None) -> RespuestaCategorias:
    request = CatalogRequest(vehiculo=vehiculo)
    url = request.to_url()

    with session_scope(headers=headers) as session:
        response = session.get(url, timeout=30)

    _ensure_ok(response)

    categorias = extract_categories(response.text)
    return RespuestaCategorias(vehiculo=vehiculo, categorias=categorias)


def _ensure_ok(response: requests.Response) -> None:
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        raise CatalogScraperError(
            f"No se pudo recuperar el catálogo desde {response.url}. Código: {response.status_code}"
        ) from exc
