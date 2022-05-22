
#закомментировал баг

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import ProductModel, CategoryModel
#from .forms import NewBookForm, RenewBookForm

def index(request):
	num_products = ProductModel.objects.all().count()
	num_categorys = CategoryModel.objects.all().count()
	products = ProductModel.objects.all()

	#print(products.content)

	return render(
		request,
		'index.html',
		context={
			'num_products': num_products,
			'num_categorys': num_categorys,
			'products': products,
		})

class ProductCreateView(CreateView):
	model = ProductModel
	fields = ('__all__')
	
class CategoryCreateView(CreateView):
	model = CategoryModel
	fields = ('__all__')

