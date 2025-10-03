from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from blog.models import Post
from portfolio.models import Portfolio

def home(request):
    latest_blog = Post.objects.order_by('-created_at').first()
    latest_portfolio = Portfolio.objects.order_by('-created_at').first()
    return render(request, "home/home.html", {
        "latest_blog": latest_blog,
        "latest_portfolio": latest_portfolio,
    })

def about(request):
    return render(request, "home/about.html")

def portfolio(request):
    return render(request, "home/portfolio_list.html")
    
def privacy(request):
    return render(request, "home/privacy.html")

def disclaimer(request):
    return render(request, "home/disclaimer.html")

def contact(request):
    return render(request, "home/contact.html")

def copyright_notice(request):
    return render(request, "home/copyright.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Build the email
            mail = EmailMessage(
                subject=f"New Contact Form Submission from {name}",
                body=f"Message:\n{message}\n\nFrom: {name} <{email}>",
                from_email=settings.DEFAULT_FROM_EMAIL,   # Displayed as contact@mitsunori.dev
                to=[settings.DEFAULT_TO_EMAIL],            # Actual Gmail account to receive the email
                reply_to=["contact@mitsunori.dev"],                         # Allows replying directly to sender
            )

            # Send the email
            mail.send()

            messages.success(request, "Your message has been sent successfully!")
            # Redirect after successful send (you can replace with a "thank you" page)
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})