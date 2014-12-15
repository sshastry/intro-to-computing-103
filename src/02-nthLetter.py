def nthLetter_nTimes(s):
    L = list(s)
    M = []
    i = 1
    for y in L:
        M.append(i*y)
        i = i + 1

    return M
