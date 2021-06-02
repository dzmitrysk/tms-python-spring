def fn(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(f"{key}:{value}")

fn(cccccc=1, a=1, bb=4, ddd=5)
