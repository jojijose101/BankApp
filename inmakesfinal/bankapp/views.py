from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormRegister
from .models import BankAccount, Branches


# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required(login_url='authapp:login')
def newpage(request):
    return render(request,'newpage.html')
@login_required(login_url='authapp:login')
def form(request):
    print(request.POST)
    if request.method == 'POST':
        forms = FormRegister(request.POST)
        if forms.is_valid():
            messages.info(request,'Application accepted')
            forms.save()
            return redirect('bankapp:form')
    else:
        forms = FormRegister()
    return render(request,'form.html',{'form':forms})
def load_branch(request):
    dist_id = request.GET.get('dist_id')
    print(dist_id)
    braches = Branches.objects.filter(dist_id=dist_id).all()
    return render(request,'branches.html',{'branches':braches})