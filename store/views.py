# Django modules
from multiprocessing import context
from django.shortcuts import render, get_object_or_404

# Django locals
from store.models import Product
from category.models import Category

# Create your views here.


def store(request,category_slug=None):

	# Define categories and products are None
	categories = None
	products   = None

	products_set_1 = None
	products_set_2 = None
	products_set_3 = None
	products_set_4 = None

	# What if categories slug are NOT None or exist
	# Return the slugs if they are exist, or
	# return 404 error if they are not exist
	if category_slug != None:
		categories = get_object_or_404(Category, slug=category_slug)
		products   = Product.objects.filter(category=categories, is_available=True)
		# Product count
		products_set_1 = Product.objects.all()[:4]
		products_set_2 = Product.objects.all()[1:5]
		products_set_3 = Product.objects.all()[2:6]
		products_set_4 = Product.objects.all()[3:7]
		product_count = products.count()
        
	else:
		# Get all the available products
		products = Product.objects.all().filter(is_available=True)
		# Counting the products
		products_set_1 = Product.objects.all()[:4]
		products_set_2 = Product.objects.all()[1:5]
		products_set_3 = Product.objects.all()[2:6]
		products_set_4 = Product.objects.all()[3:7]
		product_count = products.count()
	
	
	
	

	# Put the available products into context dictionary
	context = {
		'products':products, # <-- 'products'  as variable
		'product_count':product_count,
		'categories': categories,

		'products_set_1' : products_set_1,
		'products_set_2' : products_set_2,
		'products_set_3' : products_set_3,
		'products_set_4' : products_set_4,
		
	}	

	return render(request, 'store/store.html', context)

def product_detail(request,category_slug,product_slug):
	# Get the slug from Category model and slug from the Product model
	try: 
		single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
		products = Product.objects.all().filter(is_available=True)
		products_set_1 = Product.objects.all()[:4]
		products_set_2 = Product.objects.all()[1:5]
		products_set_3 = Product.objects.all()[2:6]
		products_set_4 = Product.objects.all()[3:7]
		
	except Exception as e: 
		raise e

	# Put the available products into context dictionary
	context = {
		'single_product':single_product, # <-- 'single_product'  as variable
		'products': products,

		'products_set_1' : products_set_1,
		'products_set_2' : products_set_2,
		'products_set_3' : products_set_3,
		'products_set_4' : products_set_4,

	}
	return render(request, 'store/product_detail.html', context)