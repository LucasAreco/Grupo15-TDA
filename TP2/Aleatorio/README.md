## Requisitos

- Python 3.10 o superior.
- No requiere sistema operativo especifico (compatible con Windows, Linux y macOS).

## Dependencias

No requiere librerias externas. Solo se utilizan modulos de la libreria estandar de Python:

- `csv`
- `os`
- `random`

## Estructura esperada

- Inputs (sets de datos en formato CSV):
	- [datasets/](datasets/)
- Output con resultados acumulados:
	- [resultados.csv](resultados.csv)

### Formato de los archivos de entrada

Cada archivo CSV dentro de la carpeta `datasets/` debe tener el siguiente formato:

n

u1,v1

u2,v2

...

Donde la primera linea indica la cantidad de vertices `n` del grafo (numerados de `0` a `n-1`), y cada linea siguiente representa una arista `(u, v)`.

Ejemplo (`dataset_k4.csv`):
4

0,1

0,2

0,3

1,2

1,3

2,3

## Uso

Desde la carpeta del proyecto, ubicarse en el mismo directorio donde se encuentra la carpeta `datasets/` y ejecutar:

```bash
python3 aleatorio.py
```
