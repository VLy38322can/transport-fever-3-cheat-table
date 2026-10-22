# Build: 2db2fadc8d3cc41d9536d9aada179bab

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
