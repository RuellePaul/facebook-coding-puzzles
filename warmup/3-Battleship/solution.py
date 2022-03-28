from typing import List


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    flatten_grid = [cell for row in G for cell in row]
    ships_count = len([cell for cell in flatten_grid if cell == 1])
    return ships_count / len(flatten_grid)
