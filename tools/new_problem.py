import sys
from pathlib import Path

ROOT = Path(".")
TEMPLATE_PATH = ROOT / "templates" / "problem_template.md"


def snake_to_pascal(s: str) -> str:
    return "".join(word.capitalize() for word in s.split("_"))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 tools/new_problem.py <problem_name>")
        sys.exit(1)

    problem_name = sys.argv[1].strip()
    if not problem_name:
        print("Problem name must not be empty")
        sys.exit(1)

    problem_dir = ROOT / "problems" / problem_name
    python_file = ROOT / "languages" / "python" / "src" / f"{problem_name}.py"
    go_file = ROOT / "languages" / "go" / "src" / f"{problem_name}.go"
    java_file = ROOT / "languages" / "java" / "src" / f"{snake_to_pascal(problem_name)}.java"
    rust_file = ROOT / "languages" / "rust" / "src" / "bin" / f"{problem_name}.rs"
    cpp_file = ROOT / "languages" / "cpp" / "src" / f"{problem_name}.cpp"
    ts_file = ROOT / "languages" / "typescript" / "src" / f"{problem_name}.ts"

    problem_dir.mkdir(parents=True, exist_ok=True)

    if TEMPLATE_PATH.exists():
        content = TEMPLATE_PATH.read_text()
        content = content.replace("<Problem Name>", problem_name.replace("_", " ").title())
        (problem_dir / "README.md").write_text(content)
    else:
        (problem_dir / "README.md").write_text(f"# {problem_name}\n")

    for path in [python_file, go_file, java_file, rust_file, cpp_file, ts_file]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

    print(f"Created scaffold for problem: {problem_name}")
    print(f"- {problem_dir / 'README.md'}")
    print(f"- {python_file}")
    print(f"- {go_file}")
    print(f"- {java_file}")
    print(f"- {rust_file}")
    print(f"- {cpp_file}")
    print(f"- {ts_file}")


if __name__ == "__main__":
    main()
