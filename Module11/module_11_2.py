import inspect

class H:
    def __init__(self):
        self.a = 0
        self.b = 2
    def hello(self):
        print('hello')

def introspection_info(obj):
    x1 = vars(obj) if '__dict__' in dir(obj) else None
    x2 = dir(obj)
    x3 = inspect.getmodule(obj)
    return {'type': type(obj).__name__,
            'attributes': x1,
            'methods': x2,
            'module': x3
            }

h = H()
someInfo = introspection_info (h)
print(someInfo)
