from ast import Pass


vector1 = input("first vector: ")
vector2 = input("second vector: ")

v1 = []
v2 = []

for i in vector1:
    v1.append(int(i))

for i in vector2:
    v2.append(int(i))

def vector_sum(v1, v2):
    sum_v = []
    for i in range(len(v1)):
        x = v1[i] + v2[i]
        sum_v.append(x)
    print(sum_v)

def dot_product(v1, v2):
    pass

vector_sum(v1, v2)