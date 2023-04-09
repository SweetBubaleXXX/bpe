import pytest


def find_fake(n: int, w: int, d: int, p: int) -> int:
    expected_weight = sum(range(1, n)) * w
    diff_weight = expected_weight - p
    if not diff_weight:
        return n
    return diff_weight // d


@pytest.mark.parametrize(
    "args,expected",
    [
        ((3, 2, 1, 4), 2),
        ((4, 5, 2, 24), 3),
        ((5, 4, 3, 37), 1),
        ((7, 3, 1, 63), 7),
    ],
)
def test_find_fake(args: tuple[int, int, int, int], expected: int):
    assert find_fake(*args) == expected
