from django.contrib import admin
from .models import Banner,Category,Brand,Size,Product,ProductAttribute



admin.site.register(Brand)
admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(Category,CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','brand','size','status','is_featured',)
    list_editable=('status','is_featured')
admin.site.register(Product,ProductAdmin)



#Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    
    list_display=('id','product','price','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)