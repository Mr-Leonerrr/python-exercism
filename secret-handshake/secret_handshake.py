CODES = ["wink", "double blink", "close your eyes", "jump"]


def commands(code: int):

    try:
        n = code if type(code) == int else int(code, 2)

    except ValueError:
        return []

    if n <= 0:
        return []

    return shake(n)


def shake(n):

    step = 1 - 2 * int(16 & n > 0)

    return [act for i, act in enumerate(CODES) if 1 << i & n][::step]
