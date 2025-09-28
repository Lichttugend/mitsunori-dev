from django.shortcuts import render, get_object_or_404
from .models import Portfolio

def portfolio_list(request):
    portfolios = Portfolio.objects.all().order_by("-created_at")
    return render(request, "portfolio/portfolio_list.html", {"portfolios": portfolios})

def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    return render(request, "portfolio/portfolio_detail.html", {"portfolio": portfolio})