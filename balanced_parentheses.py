from functools import lru_cache


@lru_cache(maxsize=None)
def match_open_close(opens, closes):
    if opens == 0:
        return {')' * closes}

    solutions = set()

    # 1, 2, 3 ... num_open
    for opens_used in range(1, opens + 1):
        openings = {
            '(' * opens_used + ')' + s
            for s in
            match_open_close(opens - opens_used, closes - 1)
        }

        # ensure not wastefully creating redundant solutions
        assert openings.isdisjoint(solutions)

        solutions = solutions.union(openings)

    closes_available = closes - opens
    # 1, 2, 3 ... closes_available
    for closes_used in range(1, closes_available + 1):
        closings = {
            ')' * closes_used + '(' + s
            for s in
            match_open_close(opens - 1, closes - closes_used)
        }

        # ensure not wastefully creating redundant solutions
        assert closings.isdisjoint(solutions)

        solutions = solutions.union(closings)

    return solutions


def balanced_parentheses(length):
    half_length = int(length/2)
    return match_open_close(half_length, half_length)
