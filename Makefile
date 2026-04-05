.PHONY: build up down shell benchmark run-python run-go run-java run-rust run-cpp run-ts

build:
	docker compose build

up:
	docker compose up -d dev

down:
	docker compose down

shell:
	docker compose exec dev bash

benchmark:
	docker compose exec dev python3 tools/benchmark.py

run-python:
	docker compose exec dev python3 languages/python/src/contains_duplicate.py

run-go:
	docker compose exec dev go run languages/go/src/contains_duplicate.go

run-java:
	docker compose exec dev bash -lc 'mkdir -p languages/java/bin && javac -d languages/java/bin languages/java/src/ContainsDuplicate.java && java -cp languages/java/bin ContainsDuplicate'

run-rust:
	docker compose exec dev cargo run --manifest-path languages/rust/Cargo.toml

run-cpp:
	docker compose exec dev bash -lc 'mkdir -p languages/cpp/bin && g++ -O2 -std=c++17 languages/cpp/src/contains_duplicate.cpp -o languages/cpp/bin/contains_duplicate && ./languages/cpp/bin/contains_duplicate'

run-ts:
	docker compose exec dev bash -lc 'cd languages/typescript && npm run build && npm run start'
