n = int(input())

colWidth = len("{0:b}".format(n))

for i in range(0, n):
    print(
        "{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(
            i + 1, width=colWidth
        ).upper()
    )
