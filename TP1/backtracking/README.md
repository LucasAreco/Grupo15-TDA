# Backtracking - Ejecucion de Casos

Este modulo permite resolver laberintos con backtracking y automatizar corridas por lote mediante el script [run.sh](run.sh).

## Requisitos

- Sistema operativo con Bash (Linux/macOS, o Git Bash en Windows).
- Python 3.10 o superior.
- Permisos de ejecucion para el script.

Si hace falta, habilitar permisos:

```bash
chmod +x run.sh
```

## Dependencias

No requiere librerias externas de Python para ejecutar el flujo principal.

- Dependencias de Python: solo librerias estandar.
- Modulos del proyecto usados por [main.py](main.py): [bt.py](bt.py).
- Herramientas de sistema: `bash`, `find`, `awk`, `tee`.

## Estructura esperada

- Inputs:
	- [data/input/basic_case](data/input/basic_case)
	- [data/input/worst_case](data/input/worst_case)
- Outputs por caso:
	- [data/output/basic_case](data/output/basic_case)
	- [data/output/worst_case](data/output/worst_case)
- CSV de resultados acumulados:
	- [data/results.csv](data/results.csv)

## Uso del script

Desde la carpeta [backtracking](.) ejecutar:

```bash
./run.sh [opciones]
```

### Opciones

- `-case <worst|basic>`: ejecuta todos los CSV de la carpeta del caso elegido.
- `-file <ruta_csv>`: ejecuta un unico archivo CSV.
- `--v`, `--verbose` o `-v`: modo verboso.
- `-h` o `--help`: muestra ayuda.

Si no se usa modo verboso, el script no imprime la salida de cada caso en consola y solo muestra al final el resumen generado desde [data/results.csv](data/results.csv).
Durante la ejecucion, igualmente se muestran mensajes de progreso por pantalla indicando que caso se esta procesando.

### Ejemplos

Ejecutar todos los casos worst_case:

```bash
./run.sh -case worst
```

Ejecutar todos los casos basic_case:

```bash
./run.sh -case basic
```

Ejecutar un unico caso:

```bash
./run.sh -file data/input/basic_case/maze.csv
```

Modo verboso:

```bash
./run.sh --v -case worst
./run.sh -v -case basic
```
