from django.db import models

#Banner 

class Banner(models.Model):
    img=models.CharField(max_length=200)
    alt_text=models.CharField(max_length=300)



#Category
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")
    
    def __str__(self):
        return self.title
    

#Brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")
    
    def __str__(self):
        return self.title
    

#Size
class Size(models.Model):
    title=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title

#PorS
class PorS(models.Model):
    title=models.CharField(max_length=100)
    value=models.CharField(max_length=100)
    def __str__(self):
        return self.title


#Product Model

class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    



#Product Attributes
class ProductAttribute(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveBigIntegerField()

    def __str__(self):
        return self.product.title
    