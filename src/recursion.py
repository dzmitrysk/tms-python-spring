a, b = 7, 10

def print_seq():
    global a, b

    if a != b:
        a += 1
        print_seq()
        print(a)
        a -= 1

a -= 1
print_seq()