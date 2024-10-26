# Dot product of two vectors

a  = [1, 2, 3]
b = [4, 5, 6]

def dot_product(a, b):
    array = []
    for i in range(len(a)):
        dot = a[i] * b[i]
        array.append(dot)
    return sum(array)

print(dot_product(a, b))


