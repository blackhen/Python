'''Lab_OneTwo'''
def onetwo(num):
    '''onetwo'''
    if num in [1, 2]:
        return str(num)
    else:
        return onetwo(num - 1) + onetwo(num - 2)
print onetwo(input()) 
