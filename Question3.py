strUnit = input ("Please enter D for distance, A for area or V for volume: ")

#print(strUnit)

if strUnit == 'D':
    print("Distance")
elif strUnit == "A":
    print ("Area")
elif strUnit == "V":
    print("Volume")
else:
    print("Invalid Choice")
    quit()

