from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fruits(req):
    # return HttpResponse('<html><body><h1>Mangoes and Grapes<h1></body><html>')
    ctx = {
        'name': "Varun YR",
        'fruits'  : ['Mango','grape', 'Apple','Orange']
    }
    return render(req,'myapp\index.html',ctx)

def PersonForm(req):
    return render(req,'myapp/personform.html')
    