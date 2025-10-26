from django import forms

class InputForm1(forms.Form):
    input1 = forms.IntegerField(min_value=2,label="Enter a Number")
    name1 = forms.CharField(max_length=25, label="Enter Name")