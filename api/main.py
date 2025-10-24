from __future__ import annotations

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import uvicorn

from models.schemas import RespuestaCategorias, Vehiculo
from scraper.catalog import CatalogScraperError, get_categories

load_dotenv()

app = FastAPI(title="RockAuto Scraper API", version="0.1.0")


@app.post("/categorias", response_model=RespuestaCategorias)
def consultar_categorias(vehiculo: Vehiculo) -> RespuestaCategorias:
    try:
        resultado = get_categories(vehiculo)
    except CatalogScraperError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return resultado


def _bool_from_env(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    reload = _bool_from_env(os.getenv("API_RELOAD"))

    uvicorn.run("api.main:app", host=host, port=port, reload=reload)
