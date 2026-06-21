
#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VERBOSE=false
CASE_TYPE=""
SINGLE_FILE=""

usage() {
    cat <<EOF
Uso:
    ./run.sh -case worst [--v|--verbose]
    ./run.sh -case basic [--v|--verbose]
    ./run.sh -file data/input/basic_case/maze.csv [--v|--verbose]
    ./run.sh -case basic -file data/input/basic_case/maze.csv [--v|--verbose]

Opciones:
  -case <worst|basic>   Ejecuta todos los archivos del caso indicado.
  -file <ruta_csv>      Ejecuta un unico archivo.
    --v, --verbose, -v    Modo verboso.
  -h, --help            Muestra esta ayuda.
EOF
}

log() {
    if [[ "$VERBOSE" == "true" ]]; then
        echo "$@"
    fi
}

progress() {
    echo "$@" >&2
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -case)
            [[ $# -ge 2 ]] || { echo "Falta valor para -case"; usage; exit 1; }
            CASE_TYPE="$2"
            shift 2
            ;;
        -file)
            [[ $# -ge 2 ]] || { echo "Falta valor para -file"; usage; exit 1; }
            SINGLE_FILE="$2"
            shift 2
            ;;
        --v|--verbose|-v)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Parametro no reconocido: $1"
            usage
            exit 1
            ;;
    esac
done

if [[ -z "$CASE_TYPE" && -z "$SINGLE_FILE" ]]; then
    echo "Debes indicar -case o -file."
    usage
    exit 1
fi

if [[ -n "$CASE_TYPE" && "$CASE_TYPE" != "worst" && "$CASE_TYPE" != "basic" ]]; then
    echo "Valor invalido para -case: $CASE_TYPE (usa worst o basic)."
    exit 1
fi

mkdir -p data/output/worst_case data/output/basic_case
: > data/results.csv

declare -a files_to_run=()
output_subdir=""

if [[ -n "$SINGLE_FILE" ]]; then
    if [[ ! -f "$SINGLE_FILE" ]]; then
        echo "No existe el archivo: $SINGLE_FILE"
        exit 1
    fi
    files_to_run+=("$SINGLE_FILE")

    if [[ "$SINGLE_FILE" == *"/worst_case/"* ]]; then
        output_subdir="worst_case"
    elif [[ "$SINGLE_FILE" == *"/basic_case/"* ]]; then
        output_subdir="basic_case"
    elif [[ -n "$CASE_TYPE" ]]; then
        output_subdir="${CASE_TYPE}_case"
    else
        echo "No se pudo inferir el tipo de caso para -file. Usa -case basic o -case worst."
        exit 1
    fi
else
    input_dir="data/input/${CASE_TYPE}_case"
    output_subdir="${CASE_TYPE}_case"

    if [[ ! -d "$input_dir" ]]; then
        echo "No existe el directorio: $input_dir"
        exit 1
    fi

    while IFS= read -r -d '' file; do
        files_to_run+=("$file")
    done < <(find "$input_dir" -maxdepth 1 -type f -name '*.csv' -print0 | sort -z)

    if [[ ${#files_to_run[@]} -eq 0 ]]; then
        echo "No se encontraron archivos CSV en $input_dir"
        exit 1
    fi
fi

log "Cantidad de casos a ejecutar: ${#files_to_run[@]}"
log "Salida de archivos: data/output/$output_subdir"

total_cases="${#files_to_run[@]}"
current_case=0

for file in "${files_to_run[@]}"; do
    current_case=$((current_case + 1))
    name="$(basename "$file")"
    output_file="data/output/${output_subdir}/${name%.*}.txt"

    progress "[${current_case}/${total_cases}] Ejecutando: $name"

    if [[ "$VERBOSE" == "true" ]]; then
        python3 -m main "$file" | tee "$output_file"
    else
        python3 -m main "$file" > "$output_file"
    fi
done

sort -t',' -k3,3n -k1,1n -k2,2n data/results.csv |
awk -F',' 'NF >= 3 { printf "Tamano laberinto %sx%s - Tiempo de ejecucion %s milisegundos\n", $1, $2, $3 }'