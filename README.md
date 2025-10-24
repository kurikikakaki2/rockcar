# RockAuto Scraper Backend

Pequeña API construida con FastAPI que expone un endpoint para consultar las
categorías disponibles para un vehículo específico dentro del catálogo de
RockAuto. Internamente utiliza `requests` y `BeautifulSoup4` para descargar y
parsear el HTML del sitio sin depender de JavaScript.

## Estructura del proyecto

```
rockcar/
├── api/
│   └── main.py
├── models/
│   └── schemas.py
├── scraper/
│   ├── catalog.py
│   ├── parser.py
│   └── session.py
├── utils/
│   └── delay.py
└── requirements.txt
```

## Uso local

1. Crear un entorno virtual y activar:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la API:

   ```bash
   uvicorn api.main:app --reload --port 8000
   ```

4. Realizar una consulta POST a `http://localhost:8000/categorias` con el
   cuerpo:

   ```json
   {
     "marca": "Toyota",
     "anio": 2018,
     "modelo": "Corolla",
     "motor": "1.8L L4",
     "id": 3441450
   }
   ```

   La respuesta contendrá la información del vehículo y la lista de categorías
   disponibles con su slug y URL completa.
