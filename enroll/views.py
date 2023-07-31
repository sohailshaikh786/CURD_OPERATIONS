from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from .form import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
  #  messages.success(request, 'Your Data has been saved successfully!')
    return render(request, 'enroll/details.html', {'form': fm,'stu':stud})

def delete_data(request , id):
    if request.method == 'POST':

        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request , id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update.html' , {'form':fm})