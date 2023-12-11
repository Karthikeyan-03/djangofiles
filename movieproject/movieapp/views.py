from django.shortcuts import render
from movieapp.forms import Movieform
from movieapp.models import Movie
# Create your views here.

# create your views

def index_view(request):
    return render(request,'movieapp/index.html')


def add_movie_view(request):
    form=Movieform()                #empty ah oru form create
    if request.method=='POST':      #with data ooda formula vilugum
        form=Movieform(request.POST)   #data user kudutha athu peru post,vaanganuna get use pannanu
    if form.is_valid():    #validate pannanum
        form.save()        #normal ahh vilugum save agum
        return index_view(request)  #after the save data,and again goto indexpage

    return render(request,'movieapp/addmovie.html',{'form':form})


def list_movie_view(request):
    movies_list=Movie.objects.all().order_by('-rating')
    return render(request,'movieapp/listmovie.html',{'movies_list':movies_list})
