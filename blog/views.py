from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Tag

def blog_list(request):
    q = request.GET.get("q")
    posts = Post.objects.filter(published=True)

    if q:
        posts = posts.filter(title__icontains=q)

    paginator = Paginator(posts, 5)  # show 5 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "tags": tags,
        "q": q,
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "post": post,
        "categories": categories,
        "tags": tags,
    }
    return render(request, "blog/blog_detail.html", context,{"post": post})