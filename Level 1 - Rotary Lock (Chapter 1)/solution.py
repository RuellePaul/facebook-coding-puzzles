from typing import List


def getMinimalPathLength(N, start, end):
    direct_path_length = abs(end - start)
    return min(direct_path_length, N - direct_path_length)


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    C = [1] + C
    return sum(getMinimalPathLength(N, C[index], C[index + 1]) for index in range(M))


if __name__ == '__main__':

    SAMPLES = [
        (3, 3, [1, 2, 3]),
        (10, 4, [9, 4, 4, 8])
    ]

    for sample in SAMPLES:
        print(getMinCodeEntryTime(*sample))
