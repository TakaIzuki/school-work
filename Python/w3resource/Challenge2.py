def calcMul(items):
    mulTotal = 1
    for i in items:
        mulTotal *= i
    return mulTotal

print("The multiple is: ",calcMul([10,20,30]))