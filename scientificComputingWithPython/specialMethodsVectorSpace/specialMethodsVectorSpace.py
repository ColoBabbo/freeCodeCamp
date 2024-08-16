class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y
    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5
        # return sum(val**2 for val in self.__dict__.values())**0.5

    def __str__(self):
        # print(f"{type(getattr(self, i) for i in vars(self))}")
        # print(f"{type(tuple(getattr(self, i) for i in vars(self)))}")
        # print(f"{type(str(tuple(getattr(self, i) for i in vars(self))))}")
        return str(tuple(getattr(self, i) for i in vars(self)))
        # return f'{self.x, self.y}'

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        print(getattr(self, 'x'))
        print(vars(self))
        print(vars(other))
        print(kwargs)
        # print(f"{kwargs2 = }")
        return self.__class__(**kwargs)
    

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

v1 = R2Vector(x=2, y=3)
v3 = R2Vector(x=6, y=8)
v2 = R3Vector(x=2, y=2, z=3)
# print(f'v1 = {v1}')
# print(f'v2 = {v2}')
v_add = v1 + v3
print(v_add)

