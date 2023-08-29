from django.shortcuts import render
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm


# view here

class HomeView(ListView):
    model = Post
    context_object_name = ''
    template_name = 'posts/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'posts/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model =  Post
    form_class = EditForm
    template_name = 'posts/update_post.html'
    # fields = ['title', 'body']
