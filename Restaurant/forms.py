from django import forms
from .models import Company,Restaurant,Category,MenuItem,BrTable,Order,OrderInfo

class BrTableForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['tableNo',]
    def __init__(self, *args, **kwargs):
        super(BrTableForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': field_name,
            })

        # Add help text for the 'name' field
      
        if field_name == 'tableNo':
            field.widget.attrs['class'] += ' custom-select'  # Add the extra CSS class  
            
class OrderInfoForm(forms.ModelForm):   
    class Meta:
        model = OrderInfo
        fields = ['tableNo','docNo']     

       
    def __init__(self, *args, **kwargs):
        super(OrderInfoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': field_name,
            }) 
        # Update the widget type for the 'docNo' field to 'hidden'
        self.fields['docNo'].widget = forms.HiddenInput()
            
            
        if not self.instance.pk:
            last_order = OrderInfo.objects.order_by('-docNo').first()
            if last_order:
                next_order_number = last_order.docNo + 1
            else:
                next_order_number = 1

            self.initial['docNo'] = next_order_number                
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'picture']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': field_name,
            })

        # Add help text for the 'name' field
        self.fields['picture'].help_text = 'upload'
        if field_name == 'picture':
            field.widget.attrs['class'] += ' custom-file-upload'  # Add the extra CSS class      

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', ]

    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': field_name,
            })



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control ',
                'id': f"{field_name}",
            })     
            
         
        # Add help text for the 'name' field
        if field_name == 'name':
            field.help_text = 'Please type Category Name'      
            
            
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'restaurants','category','picture']

    def __init__(self, *args, **kwargs):
        super(MenuItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': field_name,
            })

        # Add help text for the 'name' field
        self.fields['name'].help_text = 'Please type Menu Item Name'
        self.fields['picture'].help_text = 'upload'
        # Check if the field belongs to the 'restaurants' relationship
        if field_name == 'restaurants':
            field.widget.attrs['class'] += ' custom-select'  # Add the extra CSS class
        if field_name == 'picture':
            field.widget.attrs['class'] += ' custom-file-upload'  # Add the extra CSS class            
            

        # Add additional styling or help text for other fields if needed   
        
from .models import TempOrder        
class TempOrderForm(forms.ModelForm):
    class Meta:
        model = TempOrder
        fields = ['menu_item', 'quantity','price']  # List the fields you want to include in the form    
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu_item', 'quantity', 'price', 'mac', 'isorder']                               