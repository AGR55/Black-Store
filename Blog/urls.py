from django.urls import path
from Blog import views

urlpatterns = [
    path('blog/', views.blog, name='Blog'),
    path('blog/category/<int:category_id>/', views.category, name='Category')
]
