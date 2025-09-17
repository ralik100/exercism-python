def can_chain(dominoes):
    n = len(dominoes)
    if n == 0:
        return []

    def backtrack(chain, remaining):
        if not remaining:
            if chain[0][0] == chain[-1][1]:
                return chain
            return None

        last = chain[-1][1]  
        for i, stone in enumerate(remaining):
            a, b = stone

            if a == last:
                new_chain = chain + [stone]
                result = backtrack(new_chain, remaining[:i] + remaining[i+1:])
                if result:
                    return result

            if b == last:
                new_chain = chain + [(b, a)]
                result = backtrack(new_chain, remaining[:i] + remaining[i+1:])
                if result:
                    return result

        return None

    for i, stone in enumerate(dominoes):
        result = backtrack([stone], dominoes[:i] + dominoes[i+1:])
        if result:
            return result

    return None


input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
print(can_chain(input_dominoes))