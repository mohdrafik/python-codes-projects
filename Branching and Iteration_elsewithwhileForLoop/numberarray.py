x = 20656
h = ' '
nn = '\n'
cols_box = 3  # columns in each box
total_col_box = 3
total_col = cols_box * total_col_box  # total columns in one page
rows_box = 4  # rows in each box
total_box_inRow = 8  # total boxes in row wise is 8
total_rows = total_box_inRow * rows_box  # total rows in one pages
for i in range(1, total_rows):
    # print(h)
    for j in range(1, total_col + 1):
        print(x, end='')  # printing the x value and put one character space
        print(h, end='')  # put one character space
        print(h, end='')  # put one character space
        x = x + 1
        if j % cols_box == 0:
            print(h, end='')  # put one character space
            print(h, end='')  # put one character space
            # print(h, end='')  # put one character space
        if j % (2 * cols_box) == 0:
            print(h, end='')  # put one character space
            print(h, end='')  # put one character space
            print(h, end='')  # put one character space
            print(h, end='')  # put one character space
            print(h, end='')  # put one character space

    print(h)
    if i % rows_box == 0:
        print(h)
        print(h)
