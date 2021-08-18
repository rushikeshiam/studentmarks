from django import forms
from django.forms.widgets import HiddenInput


class AddStudentForm(forms.Form):
    
    RollNo=forms.IntegerField(label='Roll No',widget=forms.TextInput(attrs={'class':'form-control'}))
    Name=forms.CharField(label='First Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    Class=forms.CharField(label='Class Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    School=forms.CharField(label='School Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobile=forms.IntegerField(label='Mobile No',widget=forms.TextInput(attrs={'class':'form-control'}))
    Address=forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    Maths=forms.IntegerField(label='Math Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    Physics=forms.IntegerField(label='Physics Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    Chemistry=forms.IntegerField(label='Chemistry Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    Biology=forms.IntegerField(label='Biology Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    English=forms.IntegerField(label='English Marks',widget=forms.TextInput(attrs={'class':'form-control'}))

class EditStudentForm(forms.Form):
    
    RollNo=forms.IntegerField(label='Roll No',widget=forms.TextInput(attrs={'class':'form-control','readonly':'True'}))
    Name=forms.CharField(label='First Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    Class=forms.CharField(label='Class Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    School=forms.CharField(label='School Name',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobile=forms.IntegerField(label='Mobile No',widget=forms.TextInput(attrs={'class':'form-control'}))
    Address=forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    Maths=forms.IntegerField(label='Math Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    Physics=forms.IntegerField(label='Physics Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    Chemistry=forms.IntegerField(label='Chemistry Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    Biology=forms.IntegerField(label='Biology Marks',widget=forms.TextInput(attrs={'class':'form-control'}))
    English=forms.IntegerField(label='English Marks',widget=forms.TextInput(attrs={'class':'form-control'}))