import pickle

class A:
    def __init__(self, a, b):
        self.a, self.b = a, b


class B:
    def __init__(self, c, d):
        self.c, self.d = c, d


class K:
    def __init__(self, k):
        self.k = k


class E(A, B, K):
    def __init__(self, a, b, c, d, k, e):
        super().__init__(a, b) # Конструктор из класса A, аналог super(E, self).__init__(a, b)
        super(A, self).__init__(c, d) # Конструктор из класса B
        super(B, self).__init__(k)  # Конструктор из класса K
        self.e = e


e = E(1, 2, 3, 4, 5, 6)
print(dir(e))

methods = [attr for attr in dir(e) if callable(getattr(e, attr))]

print(methods)

dump_e = pickle.dumps(e)
print(dump_e)

e1 = pickle.loads(dump_e)

print(type(e1))
print(dir(e1))
print(id(e), id(e1))
e1.