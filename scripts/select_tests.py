import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DEPENDENCIES = {
    "src/pricing.py": ["src/cart.py"],
    "src/cart.py": [],
    "src/inventory.py": [],
}

TESTS = {
    "src/pricing.py": "tests/test_pricing.py",
    "src/cart.py": "tests/test_cart.py",
    "src/inventory.py": "tests/test_inventory.py",
}


def changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return result.stdout.splitlines()


def select_tests(changed):
    impacted = set(changed)

    while True:
        previous = len(impacted)
        for source, dependents in DEPENDENCIES.items():
            if source in impacted:
                impacted.update(dependents)
        if len(impacted) == previous:
            break

    selected = {
        test for source, test in TESTS.items()
        if source in impacted
    }
    return sorted(selected)


if __name__ == "__main__":
    changed = changed_files()
    selected = select_tests(changed)

    if selected:
          print(" ".join(selected))
    else:
          print(" ".join(sorted(set(TESTS.values()))))

    