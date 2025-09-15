while True:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    search = int(input("search: "))

    if rows <= 0 or cols <= 0 or search <= 0:
        break

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            a = i*j
            if a == search:
                    print(f'[{a}]', end=" ")
            else:
                print(a, end=" ")
        print() 