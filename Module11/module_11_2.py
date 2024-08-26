import inspect

class H:
    def __init__(self):
        self.a = 0
        self.b = 2
    def hello(self):
        print('hello')

def introspection_info(obj):
    x1 = dir(obj)
    x1_new = []
    for i in x1:
        if '__' not in i:
            x1_new.append(i)
    x2 = dir(obj)
    x3 = inspect.getmodule(obj)
    return {'type': type(obj).__name__,
            'attributes': x1_new,
            'methods': x2,
            'module': x3
            }

h = H()
someInfo = introspection_info (42)
print(someInfo)
