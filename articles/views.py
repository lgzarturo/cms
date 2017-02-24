# coding=utf-8
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.query_utils import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# request.user.is_authenticated() - Determina si el usuario esta autenticado
from articles.forms import ArticleForm
from articles.models import Article


def article_list(request):
    today = timezone.now()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Article.objects.all()
    else:
        queryset_list = Article.objects.active()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)
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
        "page_request_var": page_request_var,
        "today": today
    }
    return render(request, "article/list.html", context)


def article_detail(request, slug=None):
    instance = get_object_or_404(Article, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "article/detail.html", context)


def article_create(request):

    if not request.user.is_authenticated():
        raise Http404

    form = ArticleForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
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


def article_update(request, slug=None):

    if not request.user.is_authenticated():
        raise Http404

    instance = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance)
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


def article_delete(request, slug=None):

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Article, slug=slug)
    instance.delete()
    messages.success(request, "Se ha borrado correctamente.")
    return redirect("article:list")

