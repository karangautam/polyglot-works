PROBLEM ?= contains_duplicate
JAVA_CLASS := $(shell python3 -c "print(''.join(word.capitalize() for word in '$(PROBLEM)'.split('_')))" )

.PHONY: build up down shell benchmark ts-install run-python run-go run-java run-rust run-cpp run-ts

build:
	docker compose build

up:
	docker compose up -d dev

down:
	docker compose down

shell:
	docker compose exec dev bash

benchmark:
	docker compose exec dev python3 tools/benchmark.py $(PROBLEM)

ts-install:
	docker compose exec dev bash -lc 'cd languages/typescript && npm install'

run-python:
	docker compose exec dev python3 languages/python/src/$(PROBLEM).py

run-go:
	docker compose exec dev go run languages/go/src/$(PROBLEM).go

run-java:
	docker compose exec dev bash -lc 'mkdir -p languages/java/bin && javac -d languages/java/bin languages/java/src/$(JAVA_CLASS).java && java -cp languages/java/bin $(JAVA_CLASS)'

run-rust:
	docker compose exec dev cargo run --manifest-path languages/rust/Cargo.toml --bin $(PROBLEM)

run-cpp:
	docker compose exec dev bash -lc 'mkdir -p languages/cpp/bin && g++ -O2 -std=c++17 languages/cpp/src/$(PROBLEM).cpp -o languages/cpp/bin/$(PROBLEM) && ./languages/cpp/bin/$(PROBLEM)'

run-ts:
	docker compose exec dev bash -lc 'cd languages/typescript && npm run build && node dist/$(PROBLEM).js'
