from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category, Tag 



def post_list(request):
    q = (request.GET.get("q") or "").strip()

    order_field = "-created_at"
    try:
        Post._meta.get_field("created_at")
    except Exception:
        order_field = "-id"

    qs = Post.objects.all().order_by(order_field)
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))

    paginator = Paginator(qs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(
        request,
        "blog/post_list.html",
        {"page_obj": page_obj, "categories": categories, "tags": tags, "q": q},
    )



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, "blog/post_detail.html", {
        "post": post,
        "categories": categories,
        "tags": tags,
    })