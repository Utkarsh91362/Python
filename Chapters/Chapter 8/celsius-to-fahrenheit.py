'''c/5= f-32/9
or
f=((c/5)*9)+32
'''
def convert(c):
    f=((c/5)*9)+32
    return f

t=float(input("Enter the temperature in Celsius: "))
tn=convert(t)
print(f"The temperature in {t} Celsius is {tn:.1f} in fahrenheit")