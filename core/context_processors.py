from forms import PostForm


def post_form(request):
    return {'post_form': request.user.is_authenticated() and PostForm()}
