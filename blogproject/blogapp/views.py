from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, RegisterForm,CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post,Comment


def home_view(request):
    posts = Post.objects.all()
    context_obj = {
        'posts': posts
    }
    return render(request, 'index.html', context_obj)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = post.comments.all()
    new_comment=None
    if request.method=='POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()

    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post,'form':form,'new_comment':new_comment ,'comments':comments})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def RegistrationView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password']
            user = User(username=username, password=password, email=email)
            user.save()
            return redirect('login')

        else:
            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def LogoutView(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request,'logout.html',{'user':user })


def edit_post(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password']
            user = User(username=username, password=password, email=email)
            user.save()
            return redirect('login')


    else:
        pass
    render(request,'post_edit.html')




def delete_post(request,id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('home')

    return render(request,'post_delete.html')