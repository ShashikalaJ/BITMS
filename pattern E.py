def print_E(rows):
    for i in range(rows):
        for j in range(rows):
            if (i == 0 or i == rows - 1) or (i == rows // 2 and j <= rows // 2) or (j == 0 and (i != 0 and i != rows - 1)):
                print("*", end="")
            else:
                print(end=" ")
        print()

# Taking input from the user
rows = int(input("Enter the number of rows for the alphabet pattern 'E': "))
print_E(rows)
