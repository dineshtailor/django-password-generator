from django.shortcuts import render
import random
from django.http import HttpResponse 

# Create your views here.
def home(request):
  #return HttpResponse('Hello friends')
  age = 22
  return render(request,'generator/home.html', {'password':'dineshtailor','xxx':age })

def password(request):
  characters = list('abcdefghijklmnopqrstuvwxyz');
  length = int(request.GET.get('length',12))
  if request.GET.get('uppercase'):
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))   
  if request.GET.get('number'):
      characters.extend(list('1234567890'))   
  if request.GET.get('special'):
      characters.extend(list('!@#$%^&*()'))   
  passwd = ""
  for x in range(length):
     passwd += random.choice(characters);

  return render(request,'generator/password.html',{'password':passwd})

def aboutme(request):
  return render(request,'generator/aboutme.html')
