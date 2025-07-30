def alternating_sequence(count=None):
    total = 1
    if count is None:
        while True:
            if total % 2 == 0:
                yield -total
            else:
                yield total
            total += 1
    elif count is not None:
        while total < count:
            if total % 2 == 0:
                yield -total
            else:
                yield total
        raise StopIteration

generator = alternating_sequence(10)

print(*generator)