def reverse(y):
    x = ''
    i = len(y)
    while i > 0:
        x += y[ i - 1 ]
        i -= 1
    return x
print(reverse('1234abcd'))
