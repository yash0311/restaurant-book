from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.db.models import Q

User= settings.AUTH_USER_MODEL

class RestaurantLocationQuerySet(models.query.QuerySet):
	def search(self, query):
		if query:
			query= query.strip()
			return self.filter(
				Q(name__icontains=query)|
				Q(name__iexact=query) |
				Q(location__icontains=query)|
				Q(location__iexact=query) |
				Q(category__icontains=query)|
				Q(category__iexact=query)|
				Q(item__name__icontains=query)
			).distinct()
		else:
			return self


class RestaurantLocationManager(models.Manager):
	def get_queryset(self):
		return RestaurantLocationQuerySet(self.model, using=self._db)

	def search(self,query):
		return self.get_queryset().filter(name__icontains=query)

class RestaurantLocation(models.Model):
	owner 		=models.ForeignKey(User)
	name 		=models.CharField(max_length=120)
	location 	=models.CharField(max_length=120,null=True,blank=True)
	category	=models.CharField(max_length=120,null=True,blank=True)
	timestamp	=models.DateTimeField(auto_now_add=True)
	updated		=models.DateTimeField(auto_now=True)
	slug		=models.SlugField(null=True, blank=True)
	#my_own_time	=models.DateTimeField(auto_now=False auto_now_add=False)

	objects=RestaurantLocationManager()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return f"/restaurants/{self.slug}"
		return reverse("restaurants:detail",kwargs={'slug': self.slug})

	@property
	def title(self):
	    return self.name

def rl_pre_save(sender,instance,*args,**kwargs):
	# print('saving...')
	# print(instance.timestamp)
	if not instance.slug:
		instance.slug=unique_slug_generator(instance)

'''
def rl_post_save(sender,instance,*args,**kwargs):
	print('saved')
	print(instance.timestamp)
'''
pre_save.connect(rl_pre_save,sender=RestaurantLocation)
#post_save.connect(rl_post_save,sender=RestaurantLocation)

