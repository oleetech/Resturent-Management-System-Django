from django.db import models
from django.contrib.auth.models import User
# Define a model for Restaurant
class Company(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='company_pictures/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.owner:
            request = kwargs.pop('request', None)  # Get the 'request' object from kwargs
            if request and request.user.is_authenticated:
                self.owner = request.user
        super(Company, self).save(*args, **kwargs)  # Indent this line properly

        
        
    def __str__(self):
        return self.name
# Define a model for Restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    # Define a permission
 
    def __str__(self):
        return self.name
    
        
# Define a model for Menu Item
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurants = models.ManyToManyField(Restaurant,blank=True)
    picture = models.ImageField(upload_to='menu_item_pictures/', blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)    
    def __str__(self):
        return self.name
    
class Shape(models.Model):        
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name    
class Space(models.Model):        
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name    
        
class BrTable(models.Model):

    
    name = models.CharField(max_length=255)
    size=models.PositiveIntegerField(default=0)
    restaurants = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    shape=models.ForeignKey(Shape,on_delete=models.CASCADE)
    Space=models.ForeignKey(Space,on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    booked=models.BooleanField(default=False)    
    def __str__(self):
        return self.name
class OrderInfo(models.Model): 
    tableNo = models.ForeignKey(BrTable, on_delete=models.CASCADE,blank=True,default=1)
    docNo=   models.PositiveIntegerField(default=0)  
    cookOrder=models.BooleanField(default=False)  
    cookFinish=models.BooleanField(default=False)
    served=models.BooleanField(default=False)
    billed=models.BooleanField(default=False) 
    finish=models.BooleanField(default=False)            
    def save(self, *args, **kwargs):
        # Check if the docNo is already set, if not, generate it
        if not self.docNo:
            last_doc_no = OrderInfo.objects.aggregate(models.Max('docNo'))['docNo__max']
            if last_doc_no is None:
                last_doc_no = 0
            self.docNo = last_doc_no + 1

        super(OrderInfo, self).save(*args, **kwargs)    
    def __str__(self):
        return f" {self.docNo}"    
class Order(models.Model):
    orders=models.ForeignKey(OrderInfo,on_delete=models.CASCADE,blank=True,null=True)
    tableNo = models.ForeignKey(BrTable, on_delete=models.CASCADE,blank=True,default=1)
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    mac=  models.CharField(max_length=255,default='')     
    isorder=models.BooleanField(default=False)  
    docNo=models.PositiveIntegerField(default=1)   
    def __str__(self):
        return f" {self.docNo}"
    
class TempOrder(models.Model):    
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE,blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    mac=  models.CharField(max_length=255,default='')     
    isorder=models.BooleanField(default=False) 
    
    def __str__(self):
        return f" {self.mac}"

        
class OrderItem(models.Model):
    menu_item = models.ManyToManyField(MenuItem)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField(default=0)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)  # Link to the Order
    
    
        
                   
    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"  
    
