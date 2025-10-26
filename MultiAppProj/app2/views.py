from django.shortcuts import render
from app2.forms import InputForm1
# Create your views here.
def home(request):
    if request.method == "POST":
        form1 = InputForm1(request.POST)
        if form1.is_valid():
            data1 = form1.cleaned_data
            num1 = data1.get("input1")
            fact1 = fact(num1)
            return render(request,'app2/index.html',{'form1':form1,'num1':num1,'num2':fact1})
    else: 
        form1= InputForm1()
    return render(request,'app2/index.html',{'form1':form1})


def fact(n1):
    result = 1
    for i in range(1,1+n1,1):
        result = result * i
    return result
