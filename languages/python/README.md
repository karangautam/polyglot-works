# Python

Solutions and notes for Python.

## Run a program inside the container

From the project root:

```bash
docker compose exec dev python3 languages/python/src/contains_duplicate.py
```

## Run all language benchmarks

From the project root:

```bash
docker compose exec dev python3 tools/benchmark.py
```
