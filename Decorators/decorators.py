import time


def my_decorator(func):
    def wrapper(*args, **kwargs):

                
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper
    

@my_decorator
def add_nums(a, b):
    print(a+b)


def repeat(n):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print("Start")
                func(*args, **kwargs)
                print("End")
        return wrapper
    return my_decorator

@repeat(4)  
def add_nums(a, b):
    print(a+b)

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end =  time.time()

        print(end - start)
        return result
    return wrapper

@timing  
def add_nums(a, b):
    print(a+b)
    
add_nums(20, 30)

def is_authenticated(username, password):
    return username == "admin" and password == "admin"
    
def requires_auth(func):
    def wrapper(*args, **kwargs):
        if is_authenticated("admin", "admin"):
            print("authentication is done")
            func(*args, **kwargs)
    return wrapper
    
@requires_auth
def add_nums(a, b):
    print(a+b)
    
add_nums(20, 30)

