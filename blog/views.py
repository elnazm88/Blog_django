from django.shortcuts import render
from .models import Post 
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
#from django.http import HttpResponse
#home function
def home(request):
	context={
	     'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html',context)
	#return HttpResponse('<h1>Blog Home</h1>')
#home list view   
class PostListView(ListView):
	model = Post
	template_name= 'blog/home.html'
	context_object_name= 'posts'
	ordering = ['data_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(CreateView):
	model = Post	
	fields = ['title','content']

def about(request):
	return render(request, 'blog/about.html',{'title':'About'})
	#return HttpResponse('<h1>Blog about</h1>')
    