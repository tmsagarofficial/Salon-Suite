from django.db import models
from django.utils.html import mark_safe

#Banner 

class Banner(models.Model):
    img=models.ImageField(upload_to="banner_imgs/",max_length=300)
    alt_text=models.CharField(max_length=300)
    class Meta:
        verbose_name_plural='1. Banners'
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text


#Category
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/",max_length=300)
    
    
    class Meta:
        verbose_name_plural='2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.title
    

#Brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")
    
    class Meta:
            verbose_name_plural='3. Brand'

    def __str__(self):
        return self.title
    

#Size
class Size(models.Model):
    title=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='4. Sizes'
    
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
    is_featured=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='5. Prodcuts'
    



#Product Attributes
class ProductAttribute(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveBigIntegerField()
    class Meta:
        verbose_name_plural='6. Prodcut Attributes'
    def __str__(self):
        return self.product.title
    