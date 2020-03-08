class Base:
    def foo(self):
        return 'foo'

    def foo2(self):
        return self.bar2()

old_bc = __build_class__
def my_bc(*a, **kw)
    print('my build class,' *a, **kw)
    return old_bc(*a, *kw)

def my_bc(fun, name, base=None, **kw)
    if base is None:
        print('my build class,' *a, **kw)
    return old_bc(fun, name, base, **kw)

import builtins
builtins.__build_class__ = my_bc