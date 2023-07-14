class Mathematics:

    def sqr(x):
        return x * x
        

    def cube(x):
        return x * x * x
    
    def isEven(x):
        if x % 2 == 0:
            return True
        else:
            return False
        
    def isOdd(x):
        if x % 2 != 0:
            return True
        else:
            return False

    # function takes a long time
    def xToPowerOfy(x = int, y = int):    
        result = 1
        while y != 0:
            result *= x
            y -= 1

        return result    
    
    def xPercentOfy(x, y):
        return y / 100 * x

    def ascendingOrder(list=int):
        return list.sort()
    
    def descendingOrder(list=int):
        list.sort(reverse=True)
        return list
    
    def roundOff(x):   
        x // 1
        # answer is not mathematical

    def MidPoint(x1, x2, y1, y2):
        xMid = (x1 + x2) / 2
        yMid = (y1 + y2) / 2
        return f"({xMid}, {yMid})"

