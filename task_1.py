def reverse_bytes(n: int) -> int:
    return int.from_bytes(n.to_bytes(2, "big"), "little")
