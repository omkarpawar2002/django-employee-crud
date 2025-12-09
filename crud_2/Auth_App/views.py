from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def Sign_Up(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Sign_In')
    template_name = 'Auth_App/Sign_Up.html'
    context = {'form':form}
    return render(request,template_name,context)

def Sign_In(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        # print(f"User :- {user}")
        if(user is not None):
            login(request,user)
            return redirect('Show_Employee')
        return redirect('Sign_Up')
    template_name = 'Auth_App/Sign_In.html'
    context = {}
    return render(request,template_name,context)

def Sign_Out(request):
    logout(request)
    return redirect('Sign_In')