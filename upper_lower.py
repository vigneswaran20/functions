def sum_upper(x):
    z = 0
    for i in x:
        if i.isupper():
            z += 1
    return z


def sum_lower(x):
    j = 0
    for i in x:
        if i.islower():
            j += 1
    return j
    
    

def upper_lower(x):  
    
    upper = sum_upper(x)
    lower = sum_lower(x)
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (upper,lower))

upper_lower("Vigneswaran is awesome And Beautiful in his own way!!")
