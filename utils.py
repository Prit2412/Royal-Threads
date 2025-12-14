# MEDIUM RISK FILE — utils.py

def calc(a, b, c):
    # ❌ Unclear variable names
    # ❌ No type hints
    # ❌ Hard-to-read long expression
    return a + b - c * 3 / 2 + (a * c)

def load_config(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None  # ❗ Medium risk: no logging, no handling
