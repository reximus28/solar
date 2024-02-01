from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm, CustomerForm
from .models import Customer

def home_view(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/home.html')

def order_view(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if order_form.is_valid() and customer_form.is_valid():
            customer = customer_form.save()
            order = order_form.save(commit=False)
            order.customer = customer
            order.save()
            order_form.save_m2m()
            return redirect('home')
    else:
        order_form = OrderForm()
        customer_form = CustomerForm()

    return render(request, 'pages/order.html', {'order_form': order_form, 'customer_form': customer_form})

def create_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer = customer_form.save()
            return redirect('customer_list',)  # Redirect to customer detail view
    else:
        customer_form = CustomerForm()

    return render(request, 'pages/register.html', {'customer_form': customer_form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'pages/customer.html', {'customers': customers})

def update_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data
            customer = get_object_or_404(Customer)
            form = CustomerForm(request.POST, instance=customer)
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()

    return render(request, 'pages/update_customer.html', {'form': form})


def delete_customer(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()
        return redirect('customer_list')

    return render(request, 'pages/delete_customer.html')
