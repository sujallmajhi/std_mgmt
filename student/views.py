from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from .models import Person

from .models import Person
def form_list(request):
    tasks=Person.objects.all()
    context={"tasks":tasks}
    return render(request,'form_list.html',context)
    
def form_page(request):
     if request.method == "POST":
        name = request.POST.get('name')
        field= request.POST.get('field')
        age= request.POST.get('age')
        email= request.POST.get('email')
        Person.objects.create(name=name,field=field,age=age,email=email)
        return redirect('form_list')  # Redirect back to the task list
     return render(request, 'create.html')
 
def delete_form(request, pk):
    # Retrieve the task to delete by its pk
    task = Person.objects.get(pk=pk)

    # Delete the task
    task.delete()

    # Redirect to the task list after deleting
    return redirect('form_list')

def edit_form(request, pk):
    task = Person.objects.get(pk=pk) # Retrieve task
    if request.method == "POST":
        task.name = request.POST.get('name', task.name)  # Get the new title
        task.field = request.POST.get('field', task.field)  
        task.age=request.POST.get('age',task.age)
        task.email=request.POST.get('email',task.email)
        task.save()  #
        return redirect('form_list')  # Redirect to the task list
    return render(request,'edit.html',{'task':task})

