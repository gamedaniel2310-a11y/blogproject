from django import forms
from .models import Blog,Area,City

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","body"]

class CreatAreaBlog(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"



class UpdateAreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"


class CreatCityBlog(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"


class UpdateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"
