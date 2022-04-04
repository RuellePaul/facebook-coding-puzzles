from typing import List


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    return N - min(P)


if __name__ == '__main__':

    SAMPLES = [
        (3, 1, [1]),  # -> 2
        (6, 3, [5, 2, 4])  # -> 4
    ]

    for sample in SAMPLES:
        print(getSecondsRequired(*sample))
