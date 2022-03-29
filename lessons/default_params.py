"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Defaulr parameters give more flexbility to a functions"""
    # Default parameter must follow required parameters
    return x + y + z


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))