from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
     path('tags/<int:pk>/', views.tag, name='tag'),
]