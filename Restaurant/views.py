from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
 return render(request,'home.html')

from .models import Company
from .forms import CompanyForm
def company_create(request):
    company = Company.objects.all()     
    if request.method == 'POST':
        form = CompanyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company_create')
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form': form})


def setting_page(request):
    return render(request,'settings.html')

from .models import Restaurant
from .forms import RestaurantForm
def resturent_create(request):
    reaturents = Restaurant.objects.all()    
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resturent_create')
    else:
        form = RestaurantForm()
    return render(request, 'resturent_form.html', {'form': form,'reaturents': reaturents})

def resturent_detail(request, pk):
    resturent = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'resturent_detail.html', {'resturent': resturent}) 


from .models import Category
from .forms import CategoryForm
def category_create(request):
    categories = Category.objects.all()    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_create')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form,'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_create')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_update.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_create')


from .models import MenuItem
from .forms import MenuItemForm
def menuitem_create(request):
    menu = MenuItem.objects.all()

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menuitem_create')
    else:
        form = MenuItemForm()
    return render(request, 'menu_form.html', {'form': form,'menus':menu})

def menuitem_detail(request, pk):
    menuitem = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu_detail.html', {'menuitem': menuitem})


def menuitem_update(request, pk):
    menuitem = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST,request.FILES, instance=menuitem)
        if form.is_valid():
            form.save()
            return redirect('menuitem_create')
    else:
        form = MenuItemForm(instance=menuitem)
    return render(request, 'menuitem_update.html', {'form': form})


from .models import BrTable,OrderInfo
from .forms import BrTableForm,OrderInfoForm
def order_create(request):
    
    client_ip = request.META.get('REMOTE_ADDR', '')
    temporders=TempOrder.objects.filter(mac=client_ip,isorder=False)
    resturents=Restaurant.objects.all()
    categories=Category.objects.all()
    menuitems=MenuItem.objects.all()
    orderactive=Order.objects.filter(isorder=True,mac=client_ip,orders__finish=False)
    form= BrTableForm()
    br_table_form  = OrderInfoForm() 
       
    return render (request,'order.html',{"form":form,"resturents":resturents,"categories":categories,"menuitems":menuitems,"temporders":temporders,'br_table_form': br_table_form,'orderactive':orderactive})


        
from .forms import TempOrderForm
from .models import TempOrder
def add_to_temp_order(request):
    
    if request.method == 'POST':
        client_ip = request.META.get('REMOTE_ADDR', '')
        menu_item_id = request.POST.get('menu_item')
        quantity = request.POST.get('quantity')
        menu_item = MenuItem.objects.get(pk=menu_item_id)  # Replace with your MenuItem model
        price = menu_item.price
        mac = client_ip # Replace with your MAC value
        is_order = False  # You can set this to True if needed

        # Create a new TempOrder instance and save it to the database
        temp_order = TempOrder(
            menu_item=menu_item,
            quantity=quantity,
            price=price,
            mac=mac,
            isorder=is_order,
        )
        temp_order.save()

    return redirect('order_create')   

from .models import Order, OrderInfo

def add_to_order(request):
    if request.method == 'POST':
        tableform = OrderInfoForm(request.POST)
        if tableform.is_valid():
            table_no = tableform.cleaned_data['tableNo']

            # Get the id of the saved OrderInfo
            docNo = tableform.cleaned_data['docNo']
            table_info = tableform.save()  # Save the tableform instance as an OrderInfo
            # Check if a table is selected and update its 'booked' field
            if table_info.tableNo:
                table_info.tableNo.booked = True
                table_info.tableNo.save()
            mac_list = request.POST.getlist('mac[]')
            menu_item_list = request.POST.getlist('menu_item[]')
            quantity_list = request.POST.getlist('quantity[]')
            price_list = request.POST.getlist('price[]')

            # Create Order instances for each TempOrder
            for i in range(len(mac_list)):
                order_item = Order.objects.create(
                    tableNo=table_no,
                    orders=table_info,  # Set the orders field to the OrderInfo instance
                    mac=mac_list[i],
                    menu_item_id=menu_item_list[i],
                    quantity=quantity_list[i],
                    price=price_list[i],
                    isorder=True,
                )

                order_item.save()
            
            # Update TempOrder instances
            temp_orders = TempOrder.objects.filter(mac=request.META.get('REMOTE_ADDR', ''))
            for temp_order in temp_orders:
                temp_order.isorder = True
                temp_order.save()
            
            return redirect('order_create')
    return HttpResponse("Invalid request or form data", status=400)

def need_cook(request):
    orders= OrderInfo.objects.filter(cookFinish=False)
    return render(request, 'needcook_list.html', {'needcook': orders})   

def order_item(request, doc_no):
    # Retrieve the order object based on the docNo
    orderitems = Order.objects.filter(docNo=doc_no)

    # You can perform additional processing if needed

    return render(request, 'order_item.html', {'orderitems': orderitems,'orderNo':doc_no})
    
def cookfinish(request, doc_no):
    # Retrieve the order object based on the docNo
    order= OrderInfo.objects.filter(docNo=doc_no)
    order.update(cookFinish=True)
    # You can perform additional processing if needed
    orders= OrderInfo.objects.filter(cookOrder=True,cookFinish=False,)


    return render(request, 'needcook_list.html', {'needcook': orders})  


def needbill(request):

    orders= OrderInfo.objects.filter(cookFinish=True,billed=False)


    return render(request, 'needbill_list.html', {'needbill': orders})   



def billfinish(request, doc_no):
    try:
        order = OrderInfo.objects.get(docNo=doc_no)
    except OrderInfo.DoesNotExist:
        # Handle the case where the order doesn't exist
        return redirect('error_page')  # Redirect to an error page or another view

    if request.method == "GET":
        # Update the order object to set billed=True and finish=True
        order.billed = True
        order.finish = True
        order.save()

        # Check if the order has a related table
        if order.tableNo:
            order.tableNo.booked = False
            order.tableNo.save()

        # You can perform additional processing if needed

        return redirect('needbill')  # Redirect to 'needbill' view or another URL
    else:
        # Handle the case when a POST request is made
        return render(request, 'needbill_list.html', {'needbill': order})

       


def table_list(request)    :
    tables=BrTable.objects.all() 
    return render(request,'table.html',{'tables':tables})