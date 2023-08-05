from django.shortcuts import render
from .models import Category
#Home page
def home(request):
    
    return render(request,'index.html')

def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})