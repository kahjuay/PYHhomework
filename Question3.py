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

unit_of_measurement = input("Input Unit of Measurement- i.e. mm, cm, m ,km")
    if unit_of_measurement == "mm":
        print("millimeter")
    elif unit_of_measurement == "cm"
        print("centimeter")
    elif unit_of_measurement == "m"
        print("meter")
    else:
        print("Invalid Unit")

