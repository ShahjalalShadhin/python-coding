number_pad = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9),
              ("*", 0, "#"))

for row in number_pad:
    for data in row:
        print(data, end = " ")
    print()