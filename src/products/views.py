from django.shortcuts import render

from .forms import ProductForm
from .models import Product

# Create your views here.
def product_detail_view(request, *args, **kwargs):
  product_id = kwargs['id']
  obj = Product.objects.get(id=product_id)
  print(obj.featured)
  context = {
    'object': obj
  }
  return render(request, "products/product_detail.html", context)

def product_list_view(request, *args, **kwargs):
  obj = Product.objects.all()
  context = {
    'object': obj
  }
  return render(request, "products/product_list.html", context)


def product_create_view(request, *args, **kwargs):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()

  context = {
    'form': form
  }
  return render(request, "products/product_create.html", context)