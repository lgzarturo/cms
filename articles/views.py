# coding=utf-8
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# request.user.is_authenticated() - Determina si el usuario esta autenticado
from articles.forms import ArticleForm
from articles.models import Article


def article_list(request):
    queryset_list = Article.objects.all()
    paginator = Paginator(queryset_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "List",
        "object_list": queryset,
        "page_request_var": page_request_var
    }
    return render(request, "article/list.html", context)


def article_detail(request, id=None):
    instance = get_object_or_404(Article, id=id)
    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "article/detail.html", context)


def article_create(request):
    form = ArticleForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "<a href='#'>El artículo</a> se creo correctamente.", extra_tags='html_safe')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, "No se pudo crear el artículo.")
    context = {
        "title": "Crear nuevo artículo",
        "form": form
    }
    return render(request, "article/form.html", context)


def article_update(request, id=None):
    instance = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Se actualizo la información correctamente.")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, "No se pudo guardar la información.")
    context = {
        "title": "Actualizar:  " + instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "article/form.html", context)


def article_delete(request, id=None):
    instance = get_object_or_404(Article, id=id)
    instance.delete()
    messages.success(request, "Se ha borrado correctamente.")
    return redirect("article:list")

