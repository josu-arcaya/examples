Install [uv](https://docs.astral.sh/uv/)

Run the project
```bash
uv venv
uv sync

source .venv/bin/activate

AIRFLOW_HOME="$PWD" AIRFLOW__CORE__LOAD_EXAMPLES=False airflow standalone

```
