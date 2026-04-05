# Polyglot Works

Learning data structures and algorithms across multiple languages.

## Planned languages

- Python
- Go
- Java
- Rust
- C++
- TypeScript

## Project structure

- `languages/` → one folder per language
- `tools/` → helper scripts
- `benchmarks/` → benchmark config and results
- `PROGRESS.md` → personal progress tracker

## Run the benchmark suite

```bash
docker compose exec dev python3 tools/benchmark.py
```

## Start the environment

```bash
make build
make up


make shell
make benchmark
make run-python
make run-go
make run-java
make run-rust
make run-cpp
make run-ts
```
