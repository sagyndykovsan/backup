from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import QA, Question

# Create your views here.
@csrf_exempt
def qa(request):
    qas = QA.objects.all()
    if request.method == 'GET':
        print(qas)
        return render(request, "QA.html", {'question': qas})
    
    print(request.POST.get('gname'))