intQty = input ("Please enter an integer for Qty: ")
strUnit = input ("Please enter D for distance, A for area or V for volume: ")

#print(strUnit)

try:
    intQty = int(intQty)
    print (str(intQty) + " is an Integer")
except:
    print (intQty + " is not an Integer")
    quit()

if strUnit == 'D':
    print("Distance")
elif strUnit == "A":
    print ("Area")
elif strUnit == "V":
    print("Volume")
else:
    print("Invalid Choice")
    quit()



unit_of_measurement = input("Input Unit of Measurement- i.e. mm, cm, m ,km")
if unit_of_measurement == "mm":
    print("millimeter")
    intUnit = 1
elif unit_of_measurement == "cm":
    print("centimeter")
    intUnit = 10
elif unit_of_measurement == "m":
    print("meter")
    intUnit = 1000
else:
    print("Invalid Unit")

