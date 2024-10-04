from django.shortcuts import HttpResponse, render


def home(request):
    
    if request.method == 'POST':
        data = request.POST
        iq = data['iq']
        cgpa = data['cgpa']
        print(iq,cgpa)

        context = {
            "output":"Placement ho jayega"
        }

        return render(request,'home.html', context=context)
    

    return render(request, 'home.html')