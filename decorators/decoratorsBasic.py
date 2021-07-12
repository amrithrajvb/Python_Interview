#adding extra features without changing function definition


def check(func):
    def wrapper(name,age):
        if age<18:
            print(name,"not eligible for vaccination")
        else:
            return func(name,age)
    return wrapper
@check
def vaccine(name,age):
    print(name,"eligible for vaccination")
vaccine("arun",28)

@check
def eligible_check(name,age):
    print(name)
eligible_check("arjun",2)
