def tree_ref(tree , tup):
    
    if not tup:
        return tree
    
    return tree_ref(tree[0] , tup[1:])


                
tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
print(tree_ref(tree , (3,1)))
