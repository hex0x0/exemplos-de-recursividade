def inverte(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + inverte(s[:-1])
    
print(inverte('lucas'))