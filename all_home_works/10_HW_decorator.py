# Write a call_times decorator that will take a file_name as a parameter, count the number of function calls and
# write to the file in the format f'{func_name} has been called {count} times.\n'

global_dict = {}


def call_times(filename):
    def decorator(func):
        def wrapper():
            if filename in global_dict.keys():
                res = None
                for x in global_dict[filename]:
                    if x["func"] == func.__name__:
                        x["num"] = x["num"] + 1
                        res = True
                        break

                if not res:
                    global_dict[filename].append({
                        "num": 1,
                        "func": func.__name__
                    })
            else:
                global_dict[filename] = [{
                    "num": 1,
                    "func": func.__name__
                }]

            file_str = ""
            for x, y in global_dict.items():
                if x == filename:
                    for i in y:
                        file_str += i["func"] + " was called " + str(i["num"]) + " times\n"

            with open(filename, "w") as my_file:
                my_file.write(file_str)
            func()

        return wrapper

    return decorator


@call_times('foo.txt')
def foo():
    pass


@call_times('foo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
