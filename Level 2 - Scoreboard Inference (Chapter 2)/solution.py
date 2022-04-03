from typing import List


def getMinProblemCount(N: int, S: List[int]) -> int:
    mods_3 = [False] * 3
    has_one = 1 in S
    max_score = max(S)
    max_score_multiple_3 = 0

    for score in S:
        if score % 3 == 0:
            max_score_multiple_3 = max(max_score_multiple_3, score)
        mods_3[score % 3] = True

    if max_score % 3 == 0 and mods_3[1] and mods_3[2]:
        return int(max_score / 3) + 1

    if not has_one and mods_3[1] and mods_3[2] and max_score_multiple_3 != 3 * int(max_score / 3):
        return int(max_score / 3) + 2 - (1 if max_score % 3 == 1 else 0)

    return int(max_score / 3) + (1 if mods_3[1] else 0) + (1 if mods_3[2] else 0)


if __name__ == '__main__':

    SAMPLES = [
        (5, [1, 2, 3, 4, 5]),  # -> 3
        (4, [4, 3, 3, 4]),  # -> 2
        (4, [2, 4, 6, 8]),  # -> 4
        (1, [8])  # -> 3
    ]

    for sample in SAMPLES:
        print(getMinProblemCount(*sample))
