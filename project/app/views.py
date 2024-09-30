from django.shortcuts import render, redirect
from user.models import User
from app.models import *
from app.forms import *
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.db.models import Count


# Create your views here.


def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect('home')

def home(request):
    all_products = Product.objects.filter(id__gte=2)
    hot_news = Product.objects.annotate(soni=Count('comments')).order_by('-soni')[:3]
    paginators = Paginator(all_products, 4)
    page_number = request.GET.get('sahifa', 1)
    page = paginators.page(page_number)
    
    category = request.GET.get('category')
    if category:
        all_products =Product.objects.filter(category__id=category)
    d = {
        "posts" : all_products,
        "categories" : Category.objects.all(),
        'page':page,
        'news':hot_news
    }   
    if request.POST:
            id = request.POST['p_id']
            product = Product.objects.get(id=id)
            like, created = Like.objects.get_or_create(
            product = product
        )
            print(created)
            if request.user in like.user.all():
                    like.user.remove(request.user)
            else:
                    like.user.add(request.user)
                    like.save()
            return redirect('home')
    

    return render(request, 'home.html', d)

def category(request):
    form = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'category.html', {"forms":form})

def product(request):
    form = ProductForm()
    if request.POST:
        form = ProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect('home')
    return render(request, 'product.html', {"forms":form})

def comment(request):
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            c.save()
            return redirect('home')
    return render(request, 'comment.html', {"forms":form})

def savat(request):
    form = SavatForm()
    if request.POST:
        form = SavatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'savat.html', {"forms":form})

def edit(request, id):
    i = Product.objects.get(id=id)
    form = ProductForm(instance=i)
    if request.POST:
        form = ProductForm(request.POST, files=request.FILES, instance=i)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'edit.html', {"forms":form})

def register(request):
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save()
            parol = form.cleaned_data['password']
            a.set_password(parol)
            a.save()
            return redirect('home')
    return render(request, 'register.html', {"forms":form}) 

def Login(request):
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html', {"forms":form})

def Logout(request):
    logout(request)
    return redirect('login')


def detail(request, id):
    form = CommentForm()

    d = {
        "product" : Product.objects.get(id=id),
        "form" : form
    }
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            c.product = Product.objects.get(id=id)
            c.save()
            return redirect('detail', id)
    return render(request, 'detail.html', d)