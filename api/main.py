from __future__ import annotations

from fastapi import FastAPI, HTTPException

from models.schemas import RespuestaCategorias, Vehiculo
from scraper.catalog import CatalogScraperError, get_categories

app = FastAPI(title="RockAuto Scraper API", version="0.1.0")


@app.post("/categorias", response_model=RespuestaCategorias)
def consultar_categorias(vehiculo: Vehiculo) -> RespuestaCategorias:
    try:
        resultado = get_categories(vehiculo)
    except CatalogScraperError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return resultado
