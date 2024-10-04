def pascal_triangle(n, triangle=[]):
    len_triangle = len(triangle)
    if n < 1 :
        return triangle
    
    if len_triangle < n:
        if len_triangle == 0:
            triangle.append([1])
            return pascal_triangle(n, triangle)
        row = []
        last_row = triangle[len_triangle - 1]
        len_last_row = len(last_row)
        for index, value in enumerate(last_row):
            if index == 0 and index == len_last_row - 1:
                row.append(value)
                row.append(value)
                break
            elif index == 0  :
                row.append(value)
            elif index == len_last_row - 1:
                row.append(value + last_row[index - 1])
                row.append(value)
            else:
                row.append(value + last_row[index - 1])
        triangle.append(row)
        triangle = pascal_triangle(n, triangle)
    return triangle