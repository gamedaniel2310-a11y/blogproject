from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    blogs = Blog.object.all()
    context ={
        "blogs": blogs


    }
    return render(request,"index.html")

def main(request):
    return render(request,"main.html")