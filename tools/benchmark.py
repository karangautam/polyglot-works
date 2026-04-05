import json
import re
import subprocess
import sys
import time
from pathlib import Path


CONFIG_PATH = Path("benchmarks/benchmarks.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def extract_max_memory_kb(stderr_text: str):
    match = re.search(r"Maximum resident set size \(kbytes\):\s+(\d+)", stderr_text)
    if match:
        return int(match.group(1))
    return None


def snake_to_pascal(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))


def implementation_exists(language: str, problem_name: str) -> bool:
    if language == "python":
        return Path(f"languages/python/src/{problem_name}.py").exists()

    if language == "go":
        return Path(f"languages/go/src/{problem_name}.go").exists()

    if language == "java":
        class_name = snake_to_pascal(problem_name)
        return Path(f"languages/java/src/{class_name}.java").exists()

    if language == "rust":
        return Path(f"languages/rust/src/bin/{problem_name}.rs").exists()

    if language == "cpp":
        return Path(f"languages/cpp/src/{problem_name}.cpp").exists()

    if language == "typescript":
        return Path(f"languages/typescript/src/{problem_name}.ts").exists()

    return False


def build_command(language: str, problem_name: str):
    if language == "python":
        return f"python3 languages/python/src/{problem_name}.py"

    if language == "go":
        return f"go run languages/go/src/{problem_name}.go"

    if language == "java":
        class_name = snake_to_pascal(problem_name)
        return (
            "bash -lc "
            f"'mkdir -p languages/java/bin && "
            f"javac -d languages/java/bin languages/java/src/{class_name}.java && "
            f"java -cp languages/java/bin {class_name}'"
        )

    if language == "rust":
        return f"cargo run --manifest-path languages/rust/Cargo.toml --bin {problem_name}"

    if language == "cpp":
        return (
            "bash -lc "
            f"'mkdir -p languages/cpp/bin && "
            f"g++ -O2 -std=c++17 languages/cpp/src/{problem_name}.cpp "
            f"-o languages/cpp/bin/{problem_name} && "
            f"./languages/cpp/bin/{problem_name}'"
        )

    if language == "typescript":
        return (
            "bash -lc "
            f"'cd languages/typescript && "
            f"npm run build && "
            f"node dist/{problem_name}.js'"
        )

    raise ValueError(f"Unsupported language: {language}")


def run_benchmark(name: str, command: str):
    full_command = f"/usr/bin/time -v {command}"

    start = time.perf_counter()
    result = subprocess.run(
        full_command,
        shell=True,
        capture_output=True,
        text=True,
    )
    end = time.perf_counter()

    elapsed = end - start
    max_memory_kb = extract_max_memory_kb(result.stderr)

    return {
        "language": name,
        "status": "OK" if result.returncode == 0 else "FAILED",
        "returncode": result.returncode,
        "elapsed_seconds": elapsed,
        "max_memory_kb": max_memory_kb,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def main():
    problem_name = sys.argv[1] if len(sys.argv) > 1 else "contains_duplicate"

    config = load_config()
    results = []

    for language in config.keys():
        if not implementation_exists(language, problem_name):
            results.append(
                {
                    "language": language,
                    "status": "MISSING",
                    "returncode": None,
                    "elapsed_seconds": None,
                    "max_memory_kb": None,
                    "stdout": "",
                    "stderr": "",
                }
            )
            continue

        command = build_command(language, problem_name)
        print(f"Running benchmark for {language} on {problem_name}...")
        results.append(run_benchmark(language, command))

    print(f"\nBenchmark Results for {problem_name}")
    print("-" * 76)
    print(f"{'Language':<12} {'Status':<10} {'Time (s)':<12} {'Max RSS (KB)':<15}")
    print("-" * 76)

    for result in results:
        time_str = f"{result['elapsed_seconds']:.6f}" if result["elapsed_seconds"] is not None else "-"
        mem_str = str(result["max_memory_kb"]) if result["max_memory_kb"] is not None else "-"
        print(f"{result['language']:<12} {result['status']:<10} {time_str:<12} {mem_str:<15}")

    print("-" * 76)

    failed = [r for r in results if r["status"] == "FAILED"]
    if failed:
        print("\nFailures:")
        for result in failed:
            print(f"\n[{result['language']}]")
            print(result["stderr"])


if __name__ == "__main__":
    main()
