from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from articles.models import Articles


# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'
    context_object_name = 'article'


class ArticleUpdateView(UpdateView):
    model = Articles
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    context_object_name = 'article'


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'article_create.html'
    fields = ('title', 'body', 'author')

