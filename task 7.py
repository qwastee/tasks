def generate_pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  
            else:
                
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

n = int(input("Введите количество строк треугольника Паскаля: "))

pascal_triangle = generate_pascal_triangle(n)
print_pascal_triangle(pascal_triangle)