from django.shortcuts import render,redirect
from django.views import View
from .forms import TodoForm
from .models import TodoModel
from django.http import HttpResponse



# Create your views here.

class HomeView(View):
    def get(self,request):
        todo=TodoModel.objects.all()
        print(todo)
        return render(request,"home.html",{"data":todo})
    
class TodoAddView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,"todoadd.html",{"form":form})
    def post(self,request):
        form_data=TodoForm(data=request.POST)
        if form_data.is_valid():
            Title=form_data.cleaned_data.get("Title")
            Description=form_data.cleaned_data.get("Description")
            Date=form_data.cleaned_data.get("Date")
            TodoModel.objects.create(Title=Title,Description=Description,Date=Date)
            return redirect("")
        else:
            # print(form_data.errors)
            # return render(request,"product.html",{"form":form_data})
            return HttpResponse("Erorrrr")
        
class TodoListView(View):
    def get(self,request):
        todo=TodoModel.objects.all()
        print(todo)
        return render(request,"home.html",{"data":todo})
    
class TodoDeleteView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get("id")
        todo=TodoModel.objects.get(id=tid)
        todo.delete()
        return redirect("")
    
        
class TodoEditView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        print(tid)
        todo=TodoModel.objects.get(id=tid)
        form=TodoForm(initial={"Title":todo.Title,"Description":todo.Description,"Date":todo.Date})
        return render(request,"todoedit.html",{"form":form})
    def post(self,request,**kwargs):
        form_data=TodoForm(data=request.POST)
        tid=kwargs.get("id")
        todo=TodoModel.objects.get(id=tid)
        if form_data.is_valid():
            Title=form_data.cleaned_data.get("Title")
            Description=form_data.cleaned_data.get("Description")
            Date=form_data.cleaned_data.get("Date")
            todo.Title=Title
            todo.Description=Description
            todo.Date=Date
            todo.save()
            return redirect("")
        else:
            return render(request,"todoedit.html",{"form":form_data})
        
class TodoDetailsView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get("id")
        print(tid)
        todo=TodoModel.objects.get(id=tid)
        print(todo)
        return render(request,"tododetails.html",{"data":todo})
