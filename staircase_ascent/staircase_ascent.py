def f(n):
    if n <= 2:
        return (1, 1, 2)[n]
    return f(n-1) + f(n-2) + f(n-3)

if __name__ == '__main__':
    expectations = (1, 1, 2, 4, 7, 13)
    for i, x in enumerate(expectations):
        assert f(i) == x
    print("ok")
