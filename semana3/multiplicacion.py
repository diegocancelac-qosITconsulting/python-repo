def alg_multiplicacion(num1,num2):
    suma=0
    for i in range(len(str(num2))):
        suma+=num1*(int(str(num2)[len(str(num2))-i-1])*(10**(i)))
    return suma

print(alg_multiplicacion(23958233,5830))