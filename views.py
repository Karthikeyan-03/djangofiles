from django.shortcuts import render
from . import forms
# Create your views here.

#create my views

def students_view(request):
    form=forms.Studentform
    if request.method=='POST':
        form=forms.Studentform(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request,'testapp/tem.html',{'form':form})
