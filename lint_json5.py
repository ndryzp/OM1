#!/usr/bin/env python3
"""JSON5 linter for OpenMind configuration files."""
import sys
from pathlib import Path

import json5


def lint_file(filepath: str) -> bool:
    """Validate JSON5 file syntax."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json5.loads(f.read())
        print(f"✅ {filepath}")
        return True
    except Exception as e:
        print(f"❌ {filepath}: {e}")
        return False
def main() -> None:
    """Lint all JSON5 files."""
    root = Path.cwd()
    json5_files = list(root.glob("**/*.json5"))
    errors = sum(1 for f in json5_files if not lint_file(str(f)))
    sys.exit(1 if errors else 0)
if __name__ == "__main__":
    main()
