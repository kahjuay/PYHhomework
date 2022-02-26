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

initial_unit_of_measurement = input("Input Unit of Measurement- i.e. mm, cm, m ,Km")
if initial_unit_of_measurement == "mm":


unit_of_measurement = input("Input Unit of Measurement- i.e. mm, cm, m ,km")
if unit_of_measurement == "mm":
    print("millimeter")
    intUnit = 1
elif unit_of_measurement == "cm":
elif initial_unit_of_measurement == "cm":
    print("centimeter")
    intUnit = 10
elif unit_of_measurement == "m":
elif initial_unit_of_measurement == "m":
    print("meter")
    intUnit = 1000
elif initial_unit_of_measurement == "Km":
    print("Invalid Unit")
else:
    print("Invalid Input")

changed_unit_of_measurement = input("Input Changed unit of measurement- i.e. mm,cm,m,Km ")
if changed_unit_of_measurement == "mm":
    print("millimeter")
elif changed_unit_of_measurement == "cm":
    print("centimeter")
elif changed_unit_of_measurement == "m":
    print("meter")
elif changed_unit_of_measurement == "Km":
    print("Kilometer")
else:
    print("Invalid Unit")

