from django.shortcuts import render
from .models import Banner,Category,Brand,Product,ProductAttribute
#Home page
def home(request):
    banners=Banner.objects.all().order_by('-id')
    data=Product.objects.filter(is_featured=True).order_by('-id')        
    return render(request,'index.html',{'data':data,'banners':banners})

#Category list
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})

#Brand list
def brand_list(request):
    data=Brand.objects.all().order_by('-id')
    return render(request,'brand_list.html',{'data':data})

#Products list
def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('category__title','category__id')
    brands=Product.objects.distinct().values('brand__title','brand__id')
    return render(request,'product_list.html',
                {
                    'data':data,
                    'cats':cats,
                    'brands':brands,
                }
                )

