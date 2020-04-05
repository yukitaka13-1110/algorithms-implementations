def hanoi(n, src, dst, tmp):
    if n == 1:
        print("%d を %s から %s に移動" % (n, src, dst))
    else:
        hanoi(n-1, src, tmp, dst)
        print("%d を %s から %s に移動" % (n, src, dst))
        hanoi(n-1, tmp, dst, src)


def main():
    n = int(input())
    hanoi(n, "A", "C", "B")


if __name__ == "__main__":
    main()
