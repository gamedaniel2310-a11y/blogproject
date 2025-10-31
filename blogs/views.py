from gc import get_objects

from django.shortcuts import render, redirect
from .models import Blog, Area,City
from .forms import CreateBlog,UpdateBlogForm,CreatAreaBlog,UpdateAreaForm,CreatCityBlog,UpdateCityForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def index(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, "index.html", context)


# Страница создания блога
def create_blog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)
        if form.is_valid():
            form.save()
            # После успешного сохранения — возвращаемся на главную
            return redirect('index')  # имя URL для главной страницы
    else:
        form = CreateBlog()

    context = {
        "form": form
    }
    return render(request, "main.html", context)



def update_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)

    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/")
    else:
        form = UpdateBlogForm(instance=blog)

    context = {"update_form": form}
    return render(request, "update_form_blog.html", context)


def delete_blog(request, id):
    try:
        blog = Blog.objects.get(pk=id)
        blog.delete()
    except:
        return HttpResponse("не найдено")
    return redirect ('http://127.0.0.1:8000/')


def about_info_blog(request):
    return render(request,"about.html")




def area_blog(request):
    areas = Area.objects.all()
    context = {
        "areas": areas
    }
    return render(request,"area.html",context)




def area_create_blog(request):
    if request.method == 'POST':
        form = CreatAreaBlog(request.POST)
        if form.is_valid():
            form.save()
            # После успешного сохранения — возвращаемся на главную
            return redirect('http://127.0.0.1:8000/area/')  # имя URL для главной страницы
    else:
        form = CreatAreaBlog()

    context = {
        "form": form
    }
    return render(request, "area_create.html", context)


def area_update_blog(reguest,id):
    area = get_object_or_404(Area,pk=id)


    if reguest.method =='POST':
        form = UpdateAreaForm(reguest.POST,instance=area)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/area/")

    else:
            form =UpdateAreaForm(instance=area)



    context = {"update_form": form}
    return render (reguest, "update_form_blog.html",context)



def area_delete_blog(request, id):
    try:
        area = Area.objects.get(pk=id)
        area.delete()
    except:
        return HttpResponse("не найдено")
    return redirect ('http://127.0.0.1:8000/area/')



def city_blog(request):
    city = City.objects.all()
    context = {
        "cites": city
    }
    return render(request,"city.html",context)


def city_create_blog(request):
    if request.method == 'POST':
        city_form = CreatCityBlog(request.POST)
        if city_form.is_valid():
            city_form.save()
            # После успешного сохранения — возвращаемся на главную
            return redirect('http://127.0.0.1:8000/city/')  # имя URL для главной страницы
    else:
        city_form = CreatCityBlog()

    context = {
        "city_form": city_form
    }
    return render(request, "city_creat.html", context)



def city_update_blog(reguest,id):
    city = get_object_or_404(City,pk=id)


    if reguest.method =='POST':
        city_form = UpdateCityForm(reguest.POST,instance=city)
        if city_form.is_valid():
            city_form.save()
            return redirect("http://127.0.0.1:8000/city/")

    else:
        city_form = UpdateCityForm(instance=city)



    context = {"city_update_form": city_form}
    return render (reguest, "city_update.html",context)


def city_delete_blog(request, id):
    try:
        city = City.objects.get(pk=id)
        city.delete()
    except:
        return HttpResponse("не найдено")
    return redirect ('http://127.0.0.1:8000/city/')



