import uuid
from email.mime import image


from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.template.context_processors import request

from electronics.forms import ProductForm


from electronics.models import ElectronicsData
from electronics.utils import load_data, save_data


def home(request):
    products = ElectronicsData.objects.all()  # get all products
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')
def signup(request):
    return render(request, 'signup.html')
def edit_product(request):
    return render(request, 'edit_product.html')
def delete_product(request, id):
    product = get_object_or_404(ElectronicsData, pk=id)
    product.delete()
    return redirect('home')

def update_product(request, id):
    product = get_object_or_404(ElectronicsData, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # handle image uploads too
        if form.is_valid():
            form.save()
            return redirect('home')  # or wherever you list products
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # handle image uploads too
        if form.is_valid():
            form.save()
            return redirect('home')  # or wherever you list products
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
# def smartphones_view(request):
#     smartphones = Product.objects.filter(category='Smartphones')
#     return render(request, 'smartphones.html', {'products': smartphones})
#
#
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     return render(request, 'product_detail.html', {'product': product})
def details(request):
    return None