from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from mongoengine.django.auth import User
from mongoengine.django.shortcuts import get_document_or_404

from documents import Post, Comment
from forms import PostForm, CommentForm


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})


def profile(request, user_id):
    user = get_document_or_404(User, pk=user_id)
    posts_count = Post.objects.filter(user=user).count()
    return render(
        request, 'users/profile/index.html',
        {'profile': user, 'posts_count': posts_count})


def profile_posts(request, user_id):
    user = get_document_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user)
    return render(
        request, 'users/profile/posts.html', {'profile': user, 'posts': posts})


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


@login_required
def posts_post_comment(request, post_id):
    post = get_document_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.user = request.user
            post.add_comment(comment)
            return redirect(post.get_absolute_url())

    return HttpResponseBadRequest()


@login_required
def protocol(request):
    uri_parts = request.GET['uri'].split(':')

    if len(uri_parts) != 2 or uri_parts[0] != 'web+parte':
        return HttpResponseBadRequest()

    return redirect(uri_parts[1])


def api_follow_button(request):
    return render(request, 'api/js/follow_button.js',
        content_type='application/javascript')
