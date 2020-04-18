
def cached(func):
    temp = {}
    def wrapper(*args,**kwargs):
        if args not in temp:
            result = func(*args, **kwargs)
            temp[args] = result
            return result
        else:
            return temp[args]
    return wrapper

