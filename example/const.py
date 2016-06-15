def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):
    @constant
    def IP():
        return '127.0.0.1'
    @constant
    def PORT():
        return 6000