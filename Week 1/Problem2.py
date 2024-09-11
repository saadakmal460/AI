def depth(tup):
    if not isinstance(tup, tuple):
        return 0
    
    depths = [depth(item) for item in tup if isinstance(item, tuple)]
    
    return 1 + max(depths, default=0)


result = depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2))))
print(result)
