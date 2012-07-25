from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def profile_posts(request):
    return render(request, 'profile/posts.html')
