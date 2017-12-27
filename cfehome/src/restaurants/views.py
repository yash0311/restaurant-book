from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView,UpdateView
from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation

class ContactView(TemplateView):
	template_name="contact.html"

class AboutView(TemplateView):
	template_name="about.html"


class RestaurantListView(LoginRequiredMixin,ListView):
	template_name='restaurants/restaurants_list.html'
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin,DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class=RestaurantLocationCreateForm
	login_url='/login/'
	template_name='form.html'
	#success_url='/restaurants/'

	def get_context_data(self,*args, **kwargs):
		context= super(RestaurantCreateView, self).get_context_data(*args,**kwargs)
		context['title']= 'Add restaurant'
		return context

	def form_valid(self, form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name = 'restaurants/detail-update.html'

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		name=self.get_object().name
		context['title'] = f'Update {name}'
		return context


		#if you want to change slug or pk to something else like rest_id
	# def get_object(self,*args,**kwargs):
	# 	rest_id=self.kwargs.get('rest_id')
	# 	obj=get_object_or_404(RestaurantLocation,id=rest_id) #looks up in database for value against rest_id
	# 	return obj



# def home(request):	
# 	return HttpResponse(html_)
# 	#return render(request, "template", {})


	"""
def home(request):
	some_ages=[21,20,18]
	dic={
	"some_ages":some_ages
	}
	return render(request,"home.html",dic)

def about(request):
	dic={
	}
	return render(request,"about.html",dic)


def contact(request):
	dic={
	}
	return render(request,"contact.html",dic)
"""
