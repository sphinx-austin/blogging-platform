from django.shortcuts import render
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# view here
# @login_required(login_url='/members/login/')
class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    
    # @method_decorator(login_required(login_url='login'))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


# @login_required(login_url='login')
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'posts/article_details.html'


# @login_required(login_url='login')
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')


# @login_required(login_url='login')
class UpdatePostView(UpdateView):
    model =  Post
    form_class = EditForm
    template_name = 'posts/update_post.html'
    # fields = ['title', 'body']

# @login_required(login_url='login')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')
