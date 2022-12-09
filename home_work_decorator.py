global_dict = {}

def call_times(filename):
    def decorator(func):
      def wrapper():
        if func.__name__ in global_dict.keys():
          global_dict.update({func.__name__: global_dict[func.__name__] + 1})
        else:
          global_dict[func.__name__] = 1

        file_str = ""
        for x, y in global_dict.items():
          file_str += x + " was called " + str(y) + " times\n"

        with open(filename, "w") as my_file:
          my_file.write(file_str)
        func()
      return wrapper
    return decorator

@call_times("test.txt")
def foo():
  print("test_foo")

@call_times("test.txt")
def boo():
  print("test_boo")

foo()
foo()
boo()
