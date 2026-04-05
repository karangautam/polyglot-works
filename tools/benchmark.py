import json
import re
import subprocess
import time
from pathlib import Path


CONFIG_PATH = Path("benchmarks/benchmarks.json")


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def extract_max_memory_kb(stderr_text: str):
    match = re.search(
        r"Maximum resident set size \(kbytes\):\s+(\d+)", stderr_text)
    if match:
        return int(match.group(1))
    return None


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
        "returncode": result.returncode,
        "elapsed_seconds": elapsed,
        "max_memory_kb": max_memory_kb,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def main():
    config = load_config()
    results = []

    for language, details in config.items():
        print(f"Running benchmark for {language}...")
        results.append(run_benchmark(language, details["command"]))

    print("\nBenchmark Results")
    print("-" * 72)
    print(f"{'Language':<12} {'Status':<8} {'Time (s)':<12} {'Max RSS (KB)':<15}")
    print("-" * 72)

    for result in results:
        status = "OK" if result["returncode"] == 0 else "FAILED"
        time_str = f"{result['elapsed_seconds']:.6f}"
        mem_str = str(result["max_memory_kb"]
                      ) if result["max_memory_kb"] is not None else "N/A"
        print(
            f"{result['language']:<12} {status:<8} {time_str:<12} {mem_str:<15}")

    print("-" * 72)

    failed = [r for r in results if r["returncode"] != 0]
    if failed:
        print("\nFailures:")
        for result in failed:
            print(f"\n[{result['language']}]")
            print(result["stderr"])


if __name__ == "__main__":
    main()
