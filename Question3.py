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
    print("Volume2")
else:
    print("Invalid Choice")
    quit()

