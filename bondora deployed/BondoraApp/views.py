from django.shortcuts import render
from django.http import HttpResponse
import six
import sys
sys.modules['sklearn.externals.six'] = six
import joblib

def home(request):
    return render(request,"home.html")

def result(request):
    rf=joblib.load('bondora_rf.sav')
    
    lis=[]
    lis.append(request.POST['ipb'])
    lis.append(request.POST['balance'])
    lis.append(request.POST['loss'])
    lis.append(request.POST['payment'])
    lis.append(request.POST['amount'])
    lis.append(request.POST['interest'])
    lis.append(request.POST['age'])
    lis.append(request.POST['duration'])
    lis.append(request.POST['employment'])
    
    ans= rf.predict([lis])
    
    if ans == 1:
        output = 'Default!'
    else:
        output = 'Not Default!'
    
    return render(request,'result.html', {'ans':output})
    
    