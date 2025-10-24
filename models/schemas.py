from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class Vehiculo(BaseModel):
    marca: str = Field(..., description="Nombre de la marca del vehículo")
    anio: int = Field(..., ge=1886, description="Año del modelo del vehículo")
    modelo: str = Field(..., description="Modelo del vehículo")
    motor: str = Field(..., description="Descripción del motor")
    id: int = Field(..., ge=0, description="Identificador interno del vehículo en RockAuto")


class Categoria(BaseModel):
    id_html: Optional[str] = Field(None, description="Valor del atributo id en el enlace HTML de la categoría")
    nombre: str = Field(..., description="Nombre visible de la categoría en RockAuto")
    slug: str = Field(..., description="Slug utilizado por RockAuto para construir la URL de la categoría")
    url: HttpUrl = Field(..., description="URL absoluta hacia la categoría")


class RespuestaCategorias(BaseModel):
    vehiculo: Vehiculo
    categorias: List[Categoria]
