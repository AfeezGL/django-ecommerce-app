from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .forms import *
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import *
# Create your views here.

# User registration view
class SignupView(CreateView):
	form_class = SignupForm 
	template_name = 'forms.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated == True:
			return HttpResponseForbidden()

		return super(SignupView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password'])
		user.save()
		Profile.objects.create(user=user)
		return HttpResponse('you can now login')