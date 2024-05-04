from typing import Any
from django import forms

class TodoForm(forms.Form):
    Title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter the Title","Class":"form-control"}))
    Description=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter the Description","Class":"form-control"}))
    Date=forms.DateField(widget=forms.TextInput(attrs={"placeholder":"Enter the Date","Class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        Title=cleaned_data.get("Title")
        Description=cleaned_data.get("Description")
        Date=cleaned_data.get("Date")
        print(Title,Description,Date)
        return cleaned_data