def maximum(*args):
    _max = args[0]
    for arg in args[1:]:
        if arg > _max:
            _max = arg
    return _max

print(maximum(1), maximum(-100,5,900,20), maximum(0,7,-10), maximum(-5.05,-1001.2,0))