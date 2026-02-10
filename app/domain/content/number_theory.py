def euclid_alg(a: int, b: int) -> int:
    # set r_{-2}, r_{-1}
    r = dict()
    r0 = max(a, b)
    r1 = min(a, b)

    while r1 > 0:
        # r0 = q * r1 + r
        q, r = divmod(r0, r1)
        r0 = r1
        r1 = r

    return r0
