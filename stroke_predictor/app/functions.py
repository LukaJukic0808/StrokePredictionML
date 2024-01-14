def getPercentageFromInterval(age, bmi, glucose_level):
    ageIntervals = [4.0, 10.0, 16.0, 20.0, 25.0, 29.0, 33.0, 37.0, 41.0, 44.0, 48.0, 51.0, 54.0, 57.0, 60.0, 64.0, 69.0, 74.0, 79.0, 82.0]
    bmiIntervals = [17.6, 19.7, 21.2, 22.5, 23.5, 24.5, 25.5, 26.4, 27.2, 28.0, 28.9, 29.8, 30.8, 31.9, 33.1, 34.5, 36.3, 38.9, 42.9, 97.6]
    glucoseIntervals = [60.6, 65.61, 69.94, 73.65, 77.06, 79.89, 82.61, 85.37, 88.52, 91.68, 94.88, 98.52, 102.87, 108.03, 113.57, 123.15, 141.84, 187.22, 214.73, 271.74]
    agePercentage = 5
    bmiPercentage = 5
    glucosePercentage = 5
    ageUpperFlag = 0
    bmiUpperFlag = 0
    glucoseUpperFlag = 0
    for i in range(1,19):
        if(age > ageIntervals[i]):
            agePercentage = agePercentage + 5
        if(bmi > bmiIntervals[i]):
            bmiPercentage = bmiPercentage + 5
        if(glucose_level > glucoseIntervals[i]):
            glucosePercentage = glucosePercentage + 5
    if(agePercentage > 50):
        agePercentage = 100 - agePercentage
        ageUpperFlag = 1
    if(bmiPercentage > 50):
        bmiPercentage = 100 - bmiPercentage
        bmiUpperFlag = 1
    if(glucosePercentage > 50):
        glucosePercentage = 100 - glucosePercentage
        glucoseUpperFlag = 1
    
    results = {
        "agePercentage": agePercentage,
        "ageUpperFlag": ageUpperFlag,
        "bmiPercentage": bmiPercentage,
        "bmiUpperFlag": bmiUpperFlag,
        "glucosePercentage": glucosePercentage,
        "glucoseUpperFlag": glucoseUpperFlag,
    }

    return results

def minMaxScaleByType(value, type):
    minAge = 0.08
    maxAge = 82
    minBMI = 10.3
    maxBMI = 97.6
    minGlucoseLevel = 55.12
    maxGlucoseLevel = 271.74
    if(type == "age"):
        return (value-minAge)/(maxAge-minAge)
    elif(type == "bmi"):
        return (value-minBMI)/(maxBMI-minBMI)
    else:
        return (value-minGlucoseLevel)/(maxGlucoseLevel-minGlucoseLevel)