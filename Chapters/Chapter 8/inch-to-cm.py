i= int(input("ENter the measurement in inch: "))

def convert(m):
    return m*2.54

new_measurement= convert(i)
print(f"The value of measurement in {i}inch is {new_measurement:.2f}cm ")