import math

def vector_input():

    v1 = input("first vector: ")
    v2 = input("second vector: ")

    print("What do you want to do with these vectors?")
    n = input("choose from sum, dot-product, length, angle,... ") # the three dots need to be filled in when new features are added

    if n == "sum":
        print(vector_sum(v1, v2))
    elif n == "dot-product":
        print(dot_product(v1, v2))
    elif n == "length":
        print("length of vector 1 = " + str(vector_length(v1)))
        print("this is the sqrt of: " + str(vector_length(v1)**2))
        print("length of vector 2 = " + str(vector_length(v2)))
        print("this is the sqrt of: " + str(vector_length(v2)**2))
    elif n == "angle":
        print(angle(v1, v2))
    else:
        print("invallid input")

def vector_sum(v1, v2):
    sum_v = []
    for i in range(len(v1)):
        x = int(v1[i]) + int(v2[i])
        sum_v.append(x)
    return sum_v

def vector_length(vector):
    length = math.sqrt(int(vector[0])**2 + int(vector[1])**2 + int(vector[2])**2)
    return length

def dot_product(v1, v2):
    products = []
    for i in range(len(v1)):
        products.append(int(v1[i]) * int(v2[i]))

    return sum(products)

def angle(v1, v2):
    cos_angle = dot_product(v1, v2) / (vector_length(v1) * vector_length(v2))
    angle = math.acos(cos_angle)

    return angle

vector_input()