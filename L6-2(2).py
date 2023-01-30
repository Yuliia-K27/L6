def func(n):
    print(n)
    if n == 0:
        return n
    func(n - 1)

func(100)
