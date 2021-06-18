import re

#
#This program is used to calculate the time needed to save for a building/upgrade in Cookie Clicker.
#

def promptUser():
    userInput = input ("> ")
    processInput(userInput)
    print ("")
    promptUser()

def processInput(inputString):

    if ((inputString == "help") | (inputString == "info")):
        print ("Currently supported values: \n")
        print ("\tk - Thousands")
        print ("\tm - Millions")
        print ("\tb - Billions")
        print ("\tt - Trillions")
        print ("\tqa - Quadrillions")
        print ("\tqi - Quintillions")
        print ("\tsx - Sextillions")
        print ("\tsp - Septillions")
        print ("\toc - Octillions")
        print ("\tno - Nonillions")
        print ("\tdc - Decillions")
    elif (re.search("/", inputString)):
        numeratorDenominatorList = re.split("/", inputString)
        numerator = numeratorDenominatorList[0]
        denominator = numeratorDenominatorList[1]

        totalTime_Sec = castToFloat(numerator) / castToFloat(denominator)
        totalTime_Min = 0
        totalTime_Hours = 0
        totalTime_Days = 0
        totalTime_Years = 0
        
        #60sec per min
        #60min per hour
        #24 hour per day
        #86400sec per day
        #31536000 per year. Roughly, and not accounting for leap years.

        while (totalTime_Sec > 31536000):
            totalTime_Years += 1
            totalTime_Sec -= 31536000

        while (totalTime_Sec > 86400):
            totalTime_Days += 1
            totalTime_Sec -= 86400

        while (totalTime_Sec > 3600):
            totalTime_Hours += 1
            totalTime_Sec -= 3600

        while (totalTime_Sec > 60):
            totalTime_Min += 1
            totalTime_Sec -= 60

        print ("\t" + inputString + ": " + str(round(totalTime_Years, 2)) + "yr, " + str(round(totalTime_Days, 2)) + "day, " + str(round(totalTime_Hours, 2)) + "hr, " +
               str(round(totalTime_Min, 2)) + "min, " + str(round(totalTime_Sec, 2)) + "sec")

    else:
        print ("Invalid input.")

def castToFloat(inputString):
    #this method parses the string for k = thousand, m = million, etc.

    #thousands case
    if (re.search("k", inputString)):
        return (float(re.sub("k", "", inputString)) * 1000)
    #millions case
    elif (re.search("m", inputString)):
        return (float(re.sub("m", "", inputString)) * 1000000)
    #billions case
    elif (re.search("b", inputString)):
        return (float(re.sub("b", "", inputString)) * 1000000000)
    #trillions case
    elif (re.search("t", inputString)):
        return (float(re.sub("t", "", inputString)) * 1000000000000)
    #quadrillions case
    elif (re.search("qa", inputString)):
        return (float(re.sub("qa", "", inputString)) * 1000000000000000)
    #quintillions case
    elif (re.search("qi", inputString)):
        return (float(re.sub("qi", "", inputString)) * 1000000000000000000)
    #sextillions case
    elif (re.search("sx", inputString)):
        return (float(re.sub("sx", "", inputString)) * 1000000000000000000000)
    #septillions case
    elif (re.search("sp", inputString)):
        return (float(re.sub("sp", "", inputString)) * 1000000000000000000000000)
    #octillions case
    elif (re.search("oc", inputString)):
        return (float(re.sub("oc", "", inputString)) * 1000000000000000000000000000)
    #nonillions case
    elif (re.search("no", inputString)):
        return (float(re.sub("no", "", inputString)) * 1000000000000000000000000000000)
    #decillions case
    elif (re.search("dc", inputString)):
        return (float(re.sub("dc", "", inputString)) * 1000000000000000000000000000000000)

def displayHeader():
    print("=================================")
    print("=== COOKIE CLICKER CALCULATOR ===")
    print("=================================")
    print("\nEnter a division operation. Ex: 5m/2.5k, 12qa/8b...\nOr type \"help\" to view the values list")

###

displayHeader()

promptUser()



