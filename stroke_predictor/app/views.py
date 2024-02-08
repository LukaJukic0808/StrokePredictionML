from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 
from app.functions import getPercentageFromInterval, minMaxScaleByType, callEndpoint, load_to_db
from app.models import Patient


def home(request):
    context = {}

    #load_to_db()

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
        stroke, strokeProbability = callEndpoint(payload=payload)

        if (stroke == 1):
            neighbors = round(strokeProbability * 3)
        else:
            neighbors = round((1 - strokeProbability)*3)


        percentages = getPercentageFromInterval(formAge, formBMI, formGlucose)
    
        context = {
            "stroke": stroke, 
            "neighbors": neighbors, 
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
    
def stroke(request):
    stroke_data = list(Patient.objects.filter(stroke=1).values())

    return JsonResponse(stroke_data, safe=False)

def no_stroke(request):
    stroke_data = list(Patient.objects.filter(stroke=0).values())

    return JsonResponse(stroke_data, safe=False)

def filter(request):
    gender = request.GET.get('gender', 'Unavailable')
    age = request.GET.get('age', 'Unavailable')
    hypertension = request.GET.get('hypertension', 'Unavailable')
    heart_disease = request.GET.get('heart_disease', 'Unavailable')
    ever_married = request.GET.get('ever_married', 'Unavailable')
    work_type = request.GET.get('work_type', 'Unavailable')
    residence_type = request.GET.get('residence_type', 'Unavailable')
    avg_glucose_level = request.GET.get('avg_glucose_level', 'Unavailable')
    bmi = request.GET.get('bmi', 'Unavailable')
    smoking_status = request.GET.get('smoking_status', 'Unavailable')
    stroke = request.GET.get('stroke', 'Unavailable')
    stroke_data = Patient.objects.all().values()
    if(gender != 'Unavailable'):
        stroke_data = stroke_data.filter(gender=gender).values()
    if(age != 'Unavailable'):
        stroke_data = stroke_data.filter(age = age).values()
    if(hypertension != 'Unavailable'):
        stroke_data = stroke_data.filter(hypertension = hypertension).values()
    if(heart_disease != 'Unavailable'):
        stroke_data = stroke_data.filter(heart_disease = heart_disease).values()
    if(ever_married != 'Unavailable'):
        stroke_data = stroke_data.filter(ever_married = ever_married).values()
    if(work_type != 'Unavailable'):
        stroke_data = stroke_data.filter(work_type = work_type).values()
    if(residence_type != 'Unavailable'):
        stroke_data = stroke_data.filter(residence_type = residence_type).values()
    if(avg_glucose_level != 'Unavailable'):
        stroke_data = stroke_data.filter(avg_glucose_level = avg_glucose_level).values()
    if(bmi != 'Unavailable'):
        stroke_data = stroke_data.filter(bmi = bmi).values()
    if(smoking_status != 'Unavailable'):
        stroke_data = stroke_data.filter(smoking_status = smoking_status).values()
    if(stroke != 'Unavailable'):
        stroke_data = stroke_data.filter(stroke = stroke).values()
        
    stroke_data = list(stroke_data)

    return JsonResponse(stroke_data, safe=False)





