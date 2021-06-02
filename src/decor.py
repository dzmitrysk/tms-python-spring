def enchancer(d): # Декоратор с параметром
    def appender(func):
        def wrapper(*args, **kwargs):
            print(d)
            func(*args, **kwargs)
            print(d)
        return wrapper
    return(appender)

@enchancer("------------")
def hello(s):
    print(s)


hello("Tratatatata")