from django.http import HttpResponse
from django.shortcuts import render
from .forms import CarForm
from .models import CarModel


# Create your views here.

def index(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        print("Going to POST in index function")

        if (form.is_valid()):
            print("The data is clean") #RECEIVING NULL ERROR ON YEAR FIELD. NOT SURE WHY
            CarModel.objects.create(make=request.POST['make'], model=request.POST['model'], year=request.POST['year'],
                                    mpg=request.POST['mpg'])

        else:#DISPLAYS ERRORS BOTH IN CONSOLE AND ON PAGE
            print(form.errors)
            allEntries = CarModel.objects.all()
            context = {
                'errors': form.errors,
                'allEntries': allEntries,
                'form': form,
            }
            return render(request, 'ValidationCWapp/index.html', context)

    allEntries = CarModel.objects.all()
    form = CarForm()
    context = {        ###############RENDERS ALL CARS ON PAGE
        'allEntries': allEntries,
        'form': form,

    }
    return render(request, 'ValidationCWapp/index.html', context)


# def congrats(request):
#     return HttpResponse('congrats')
