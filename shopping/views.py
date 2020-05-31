from django.shortcuts import render, get_object_or_404
from .models import 产品列表,商品类别表
# Create your views here.


def 主页(request):
	Allcategories = 商品类别表.objects.all()
	cate_com = []
	for 每个类别 in Allcategories:
		cate_com.append((每个类别, 产品列表.objects.filter(所属类别=每个类别, 已上架=True)[:3]))
	content = {'cate_com': cate_com, 'Allcategories': Allcategories}
	return render(request, 'shopping/home.html', content)


def 单类页(request, Eachcategory_id):
	Allcategories = 商品类别表.objects.all()
	所需类别 = get_object_or_404(商品类别表, id=Eachcategory_id)
	cate_com = [(所需类别, 产品列表.objects.filter(所属类别=所需类别, 已上架=True)[:8])]
	content = {'cate_com': cate_com, 'Allcategories': Allcategories}
	return render(request, 'shopping/home.html', content)


def 详情页(request, Eachcategory_id, 每个商品_id):
	Allcategories = 商品类别表.objects.all()
	product = get_object_or_404(产品列表, id=每个商品_id, 已上架=True)
	content = {'product': product, 'Allcategories': Allcategories}
	return render(request, 'shopping/detail.html', content)

