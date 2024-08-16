def taum_birthday(b, w, bc, wc, z) -> int:
    black_cost = b * bc
    white_cost = w * wc
    if abs(bc - wc) > z:
        if bc > wc:
            black_cost = (wc * b) + (b * z)
        else:
            white_cost = (bc * w) + (w * z)
    return black_cost + white_cost
