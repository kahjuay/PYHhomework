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
    intDim = 1
    print("Distance")
elif strUnit == "A":
    intDim = 2
    print ("Area")
elif strUnit == "V":
    intDim = 3
    print("Volume")
else:
    print("Invalid Choice")
    quit()

initial_unit_of_measurement = input("Input Unit of Measurement- i.e. mm, cm, m ,Km")
if initial_unit_of_measurement == "mm":
    print("millimeter")
    intUnit = 1

elif initial_unit_of_measurement == "cm":
    print("centimeter")
    intUnit = 10

elif initial_unit_of_measurement == "m":
    print("meter")
    intUnit = 1000

elif initial_unit_of_measurement == "Km":
    intUnit = 1000000
    print("Kilometer")
else:
    print("Invalid Input")

changed_unit_of_measurement = input("Input Changed unit of measurement- i.e. mm,cm,m,Km ")
if changed_unit_of_measurement == "mm":
    print("millimeter")
    intChangeUnit = 1

elif changed_unit_of_measurement == "cm":
    print("centimeter")
    intChangeUnit = 10

elif changed_unit_of_measurement == "m":
    print("meter")
    intChangeUnit = 1000

elif changed_unit_of_measurement == "Km":
    print("Kilometer")
    intChangeUnit = 1000000
else:
    print("Invalid Unit")

#print (intQty, intDim, intUnit, intChangeUnit)



def CalculateOutput(intQty, intDim, intUnit, intChangeUnit):
    print (((intQty/intChangeUnit)*intUnit)**intDim)

CalculateOutput (intQty, intDim, intUnit, intChangeUnit)