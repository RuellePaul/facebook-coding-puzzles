def getWrongAnswers(N: int, C: str) -> str:
    return ''.join('A' if char == 'B' else 'B' for char in C)
