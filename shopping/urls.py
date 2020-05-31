from django.urls import path
from . import views


app_name = "shopping"
urlpatterns = [
	path('',views.主页, name='主页'),
	path('<Eachcategory_id>/', views.单类页, name='单类页'),
	path('<Eachcategory_id>/<每个商品_id>/', views.详情页, name='详情页'),
]
