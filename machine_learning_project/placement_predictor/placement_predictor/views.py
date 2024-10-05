from django.shortcuts import HttpResponse, render
import joblib


def read_model(arr):
    model_logistic = joblib.load('placement_predictor/model/placement_predictor.joblib')
    scaler = joblib.load('placement_predictor/model/scaler.joblib')

    scaled_data = scaler.transform(arr)
    result = model_logistic.predict(scaled_data)

    return result

def home(request):
    
    if request.method == 'POST':
        data = request.POST
        cgpa = data['cgpa']
        iq = data['iq']
        # print(iq,cgpa)

        res = read_model([[cgpa,iq]])
        print(res)
        if res[0] == 1:
            context = {
                "output":"Placement ho jayega"
            }
        else:
            context = {
                "output":"Placement nahi hoga bhai"
            }


        return render(request,'home.html', context=context)
    

    return render(request, 'home.html')


