from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from app.functions import getPercentageFromInterval, minMaxScaleByType


def home(request):
    context = {}
    return render(request, 'app/home.html', context)

def form(request):
    context = {
        "errorMessage": ""
    }
    return render(request, 'app/form.html', context)

def result(request):
    
    if request.method == 'POST':

        if(request.POST['age'] == ''):
            context = {
            "errorMessage": "Missing age input"
            }
            return render(request, 'app/form.html', context)
        
        if(request.POST['avg_glucose_level'] == ''):
            context = {
            "errorMessage": "Missing average glucose level input"
            }
            return render(request, 'app/form.html', context)
        
        if(request.POST['bmi'] == ''):
            context = {
            "errorMessage": "Missing body mass index (BMI) input"
            }
            return render(request, 'app/form.html', context)
        
        formAge = int(request.POST['age'])
        formBMI = int(request.POST['bmi'])
        formGlucose = int(request.POST['avg_glucose_level'])

        if(formAge<0 or formAge>115):
            context = {
            "errorMessage": "Invalid age input"
            }
            return render(request, 'app/form.html', context)
        
        if(formGlucose<40 or formGlucose>350):
            context = {
            "errorMessage": "Invalid average glucose level input"
            }
            return render(request, 'app/form.html', context)
        
        if(formBMI<6 or formBMI>200):
            context = {
            "errorMessage": "Invalid body mass index (BMI) input"
            }
            return render(request, 'app/form.html', context)

        payload = {
            "gender": 0,	
            "age": 0,	
            "hypertension": 0,	
            "heart_disease": 0,	
            "ever_married": 0,	
            "avg_glucose_level": 0,	
            "bmi": 0,	
            "Govt_job": 0,	
            "Never_worked": 0,	
            "Private": 0,	
            "Self-employed": 0,	
            "children": 0,	
            "Rural": 0,	
            "Urban": 0,	
            "formerly smoked": 0,	
            "never smoked": 0,	
            "smokes": 0,
        }

        payload['age'] = minMaxScaleByType(formAge, "age")
        payload['bmi'] = minMaxScaleByType(formBMI, "bmi")
        payload['avg_glucose_level'] = minMaxScaleByType(formGlucose, "glucose")

        if(request.POST['gender']=='male'):
            payload['gender'] = 1

        if ("hypertension" in request.POST):
            payload['hypertension'] = 1

        if ("heart_disease" in request.POST):
            payload['heart_disease'] = 1

        if ("ever_married" in request.POST):
            payload['ever_married'] = 1

        payload[request.POST['work_type']] = 1
        payload[request.POST['Residence_type']] = 1
        payload[request.POST['smoking_status']] = 1

        ######## API zahtjev #############

        percentages = getPercentageFromInterval(formAge, formBMI, formGlucose)
    
        context = {
            "stroke": 0, #ovo treba bit iz apia
            "neighbors": 3, #ovo treba bit iz apia
            "age": formAge,
            "bmi": formBMI,
            "avg_glucose_level": formGlucose,
            "gender": request.POST['gender'].capitalize(),
            "hypertension": payload['hypertension'],
            "heart_disease": payload['heart_disease'],
            "ever_married": payload['ever_married'],
            "work_type": request.POST['work_type'],
            "Residence_type": request.POST['Residence_type'],
            "smoking_status": request.POST['smoking_status'].capitalize(),
            "agePercentage": percentages["agePercentage"],
            "ageUpperFlag": percentages["ageUpperFlag"],
            "bmiPercentage": percentages["bmiPercentage"],
            "bmiUpperFlag": percentages["bmiUpperFlag"],
            "glucosePercentage": percentages["glucosePercentage"],
            "glucoseUpperFlag": percentages["glucoseUpperFlag"],
        }

        return render(request, 'app/result.html', context)
    
    else:
        return HttpResponseRedirect(reverse('app:home'))




