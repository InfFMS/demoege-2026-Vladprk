for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f = (x or y) and  not(y == z) and not(w)
                if f:
                    print(w, x, y, z)