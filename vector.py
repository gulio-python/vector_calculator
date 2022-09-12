def vector_input():

    v1 = []
    v2 = []

    vector1 = input("first vector: ")
    vector2 = input("second vector: ")

    for i in vector1:
        v1.append(int(i))

    for i in vector2:
        v2.append(int(i))

    print("What do you want to do with these vectors?")
    n = input("choose from sum, dot-product,... ") # the three dots need to be filled in when new features are added

    if n == "sum":
        vector_sum(v1, v2)
    elif n == "dot-product":
        dot_product(v1, v2)
    else:
        print("invallid input")

def vector_sum(v1, v2):
    sum_v = []
    for i in range(len(v1)):
        x = v1[i] + v2[i]
        sum_v.append(x)
    print(sum_v)

def vector_length(v1, v2):
    pass

def angle(v1, v2):
    pass

def dot_product(v1, v2):
    pass

vector_input()