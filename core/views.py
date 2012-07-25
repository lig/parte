from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from mongoengine.django.shortcuts import get_document_or_404

from documents import Post
from forms import PostForm


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})


def profile_posts(request):
    return render(request, 'profile/posts.html')


@login_required
def posts_new(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post(**form.cleaned_data)
            post.pk = post.pk or None
            post.user = request.user
            post.save()
            return redirect(post.get_absolute_url())

    else:
        form = PostForm()

    return render(request, 'posts/form.html', {'form': form})


def posts_post(request, post_id):
    post = get_document_or_404(Post, pk=post_id)
    return render(request, 'posts/post.html', {'post': post})
