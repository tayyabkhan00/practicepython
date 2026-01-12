def generate(numRows):
    triangle = []                       # 1

    for row in range(numRows):          # 2
        current = [1] * (row + 1)       # 3

        for col in range(1, row):       # 4
            current[col] = (
                triangle[row - 1][col - 1] +
                triangle[row - 1][col]
            )                            # 5

        triangle.append(current)        # 6

    return triangle                     # 7
