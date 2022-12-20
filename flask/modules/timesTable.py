def cal(num):
    result=[]
    for x in range(num):
        for y in range(9):
            cal = (x+1) * (y+1)
            calResult = {
                "firstNum":x+1,
                "secondNum":y+1,
                "resultNum":cal
            }
            result.append(calResult)
    return result