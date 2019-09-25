from django.db import models
from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	time = models.DateTimeField()
	
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'time')
	
admin.site.register(BlogPost, BlogPostAdmin)

	

