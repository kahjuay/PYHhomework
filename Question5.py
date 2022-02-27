mark_1 = [46 , 41, 74, 53, 31, 39, 49, 57, 76, 80, 78, 38, 31, 56, 98, 55, 41, 73, 23, 88, 55, 60, 33, 40]
print(len(mark_1),"Digits in list")
mark_2 = [69, 48, 50, 95, 87, 11, 28, 36, 25, 70, 25, 54, 33, 42, 27, 24, 44, 20, 61, 43, 30, 44, 7, 21]
print(len(mark_2),"Digits in list")


mark_1.sort(reverse=True)
mark_2.sort(reverse=True)


egstr = [39,45,66,68,75]

intA = 70
intB = 60
intC = 55
intD = 50
intE = 45
intS = 40

cntA = 0
cntB = 0
cntC = 0
cntD = 0
cntE = 0
cntS = 0
cntU = 0

strList = egstr

print (strList)

for item in strList:
    print(item)
    if item >= intA:
        print("Grade A")
        cntA = cntA + 1
    elif item >= intB:
        print("Grade B")
        cntB = cntB + 1
    elif item >= intC:
        print("Grade C")
        cntC = cntC + 1
    elif item >= intD:
        print("Grade D")
        cntD = cntD + 1
    elif item >= intE:
        print("Grade E")
        cntE = cntE + 1
    elif item >= intS:
        print("Grade S")
        cntS = cntS + 1
    else:
        print("Grade U")
        cntU = cntU + 1

print (cntA, cntB)

