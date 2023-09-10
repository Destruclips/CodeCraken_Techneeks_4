from django.shortcuts import render
from mainapp.models import Contact_info

from joblib import load

covid_model = load('./models/covid.joblib')
heart_disease_model=load('./models/heart-disease.joblib')

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']
        ins = Contact_info(name= name, email= email, Query= query)
        ins.save()
    return render(request, 'contact.html')

def covid(request):
    return render(request, 'covid.html')

def heart(request):
    return render(request, 'heart_disease.html')

def heart_result(request):
    disease = ''
    if request.method=='POST':
        age = request.POST['age']
        age=int(age)/100
        gender=request.POST['Gender']
        chestpain = request.POST['chestpain']
        Blood_Pressure = request.POST['Blood-Pressure']
        cholesterol = request.POST['cholesterol']
        heart_rate = request.POST['heart-rate']
        angina = request.POST['angina']
        st = request.POST['st']
        thal = request.POST['thal']
        vessels = request.POST['vessels']
        array=[age, gender,chestpain, Blood_Pressure, cholesterol,0,0, heart_rate, angina, st,0, vessels,thal]
        y_pred = heart_disease_model.predict([array])[0]
        heart_prob = heart_disease_model.predict_proba([array])[0]
        if y_pred==0:
            result_heart="You don't have Heart Disease"
            prob = round(heart_prob[0]*100, 2)
            if prob>80:
                disease="Congratulations! You're safe and healthy"        
        else:
            result_heart="You have Heart Disease"
            prob = round(heart_prob[1]*100, 2)
            if prob>80:
                disease="We advice you to consult a doctor and get yourself checked immediately"

        return render(request, 'result.html',{'result':result_heart, 'probability': prob, 'disea': disease})

def covid_result(request):
    disease = ''
    if request.method=='POST':
        Gender = request.POST['Gender']
        age = request.POST['age']
        age = int(age)/100
        fever = request.POST['fever']
        cough = request.POST['cough']
        runnynose = request.POST['runnynose']
        musclesore = request.POST['musclesore']
        Pneumonia = request.POST['Pneumonia']
        Diarrhea = request.POST['Diarrhea']
        Lung = request.POST['Lung']
        travel = request.POST['travel']
        features =[Gender, age, fever, cough, runnynose, musclesore, Pneumonia, Diarrhea, Lung, travel,0]
        y_pred = covid_model.predict([features])[0]
        covid_prob=covid_model.predict_proba([features])[0]
        if y_pred == 0:
            result_covid = "You don't have Covid-19 disease"
            prob = round(covid_prob[0]*100, 2)
            if prob>80:
                disease="Congratulations! You're safe and healthy"
        else:   
            result_covid = "You have Covid-19 disease"
            prob = round(covid_prob[1]*100, 2)
            if prob>80:
                disease="We advice you to consult a doctor and get yourself checked immediately"

        return render(request, 'result.html', {'result' : result_covid, 'probability':prob, 'disea':disease})