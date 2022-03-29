import itertools


def distance(i, j):
    return abs(i - j)


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    P_indexes = []
    A_indexes = []
    B_indexes = []

    for index, cell in enumerate(C):
        if cell == 'P':
            P_indexes.append(index)
        elif cell == 'A':
            A_indexes.append(index)
        elif cell == 'B':
            B_indexes.append(index)

    photographs = list(itertools.product(*[P_indexes, A_indexes, B_indexes]))

    artistic_photographs_count = 0

    for photography in photographs:
        P_index = photography[0]
        A_index = photography[1]
        B_index = photography[2]

        if X <= distance(P_index, A_index) <= Y and X <= distance(B_index, A_index) <= Y \
                and (P_index < A_index < B_index or B_index < A_index < P_index):
            artistic_photographs_count += 1

    return artistic_photographs_count


if __name__ == '__main__':

    SAMPLES = [
        (5, 'APABA', 1, 2),
        (5, 'APABA', 2, 3),
        (8, '.PBAAP.B', 1, 3)
    ]

    for sample in SAMPLES:
        print(getArtisticPhotographCount(*sample))
