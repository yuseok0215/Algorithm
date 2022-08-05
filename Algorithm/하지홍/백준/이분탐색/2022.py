from math import sqrt

def get_height(x,y,width):
    h1 = sqrt(x**2-width**2)
    h2 = sqrt(y**2-width**2)
    c = h1*h2/(h1+h2)
    
    return c

def start():
    x, y, c = map(float, input().split())
    left= 0
    right = min(x,y)
    result = 0
    while right-left > 1e-6:
        width = (right+left)/ 2
        result = width
    
        if get_height(x,y,width) >= c:
            left = width
        else:
            right = width
    print(result)

start()
    
    
    