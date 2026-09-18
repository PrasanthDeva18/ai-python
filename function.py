def fname():
    print("hello world")

fname()


def add(a,b):
    return a + b


a = add(5,10)

print(a)


def fn2(a, b = "test"):
    print(f"{a} {b}")

fn2("hello")

fn2("hello", "world")


# argument swapping
def fn3(a, b = "test"):
    print(f"{a} {b}")

fn3(b= "temp", a = "hello")


# arbitary arguments - used for n number of argument by user


# its return like a tuple
def fn4(*args):
    print(sum(args))


fn4(1,2,3,4)


def fn5(**kwargs):
    print(kwargs)

fn5(name="prasanth", rollno="80")

# o/p - {'name': 'prasanth', 'rollno': '80'}

# **kwargs this is used for dictionary


