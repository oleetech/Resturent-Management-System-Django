from django.contrib import admin
from .models import Category,Restaurant,MenuItem,Company,Shape,Space,BrTable,TempOrder,Order,OrderInfo

class OrderInline(admin.TabularInline):
    model = Order
    exclude=['tableNo','mac','isorder']
    extra = 0
    
@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    inlines = [OrderInline] 
       
# Register your models here.
admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Company)
admin.site.register(Shape)
admin.site.register(Space)
admin.site.register(BrTable)
admin.site.register(TempOrder)
admin.site.register(Order)

