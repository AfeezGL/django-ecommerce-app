from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from account.models import Customer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
class IndexView(ListView):
	model = Product
	template_name = "index.html"
	paginate_by = 9

	def get_queryset(self):
		return Product.objects.order_by("date_created")
		
# product detail view
class ProductDetailView(DetailView):
    model = Product
    template_name = "details.html"

# Add to cart view
def add_to_cart(request):
	data = json.loads(request.body)
	product_id = data["productId"]
	session_id = request.COOKIES["sessionid"]
	product = Product.objects.get(id = product_id)
	try:
		customer = Customer.objects.get(user = request.user)
	except:
		customer, created = Customer.objects.get_or_create(session_id = session_id)
	order, created = Order.objects.get_or_create(customer = customer, completed = False)
	cartitem, created = CartItem.objects.get_or_create(product = product, customer = customer, order = order)
	cartitem.units = (cartitem.units + 1)
	cartitem.save()
	units = cartitem.units
	total = order.total
	res = {
		"total":total,
		"units":units
	}
	print (res)
	return JsonResponse(res, safe=False)

#Cart View. Shows all cart items and total
def CartView(request):
	template = "cart.html"
	try:
		customer = Customer.objects.get(user = request.user)
	except:
		session_id = request.COOKIES["sessionid"]
		customer, created = Customer.objects.get_or_create(session_id = session_id)
	order, created = Order.objects.get_or_create(customer = customer, completed = False)
	cartitems = order.cartitem_set.all()
	return render(request, template, {"order":order,
	"cartitems":cartitems})

def RefreshNum(request):
	data = json.loads(request.body)
	session_id = request.COOKIES["sessionid"]
	try:
		customer = Customer.objects.get(user = request.user)
	except:
		customer, created = Customer.objects.get_or_create(session_id = session_id)
	order, created = Order.objects.get_or_create(customer = customer, completed = False)
	cartitems = order.cartitem_set.all()
	num = 0
	for cartitem in cartitems:
		num += cartitem.units
	print (num)
	return JsonResponse(num, safe=False)

# Reduce cartitem units
def reduce_units(request):
	data = json.loads(request.body)
	product_id = data["productId"]
	session_id = request.COOKIES["sessionid"]
	product = Product.objects.get(id = product_id)
	try:
		customer = Customer.objects.get(user = request.user)
	except:
		customer, created = Customer.objects.get_or_create(session_id = session_id)
	order, created = Order.objects.get_or_create(customer = customer, completed = False)
	cartitem, created = CartItem.objects.get_or_create(product = product, customer = customer, order = order)
	cartitem.units = (cartitem.units - 1)
	if cartitem.units >= 1:
		cartitem.save()
		units = cartitem.units
	else:
		cartitem.delete()
		units = 0
	total = order.total
	res = {
		"total":total,
		"units":units
	}
	print (res)
	return JsonResponse(res, safe=False)