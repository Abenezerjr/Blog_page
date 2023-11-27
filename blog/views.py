from django.shortcuts import render
from datetime import date
from . models import Post

all_posts = [

]


def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def post(request):
    return render(request, "blog/all-post.html", {
        "all_post": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
