from django.shortcuts import render, get_object_or_404

from games.models import FeaturedGame, News, LaunchGame, Video, Game


def index(request):
    featured_games = FeaturedGame.objects.order_by("?")[:6]
    top_news = News.objects.order_by("-timestamp")[:3]
    news = News.objects.exclude(pk__in=top_news).order_by("-timestamp")[:10]
    launch_games = LaunchGame.objects.order_by("-date")[:8]
    video = Video.objects.order_by("-timestamp").first()
    if video:
        videos = Video.objects.exclude(pk=video.id).order_by("-timestamp")[:4]
    else:
        videos = Video.objects.order_by("-timestamp")[:4]

    context = {
        "title": "MiraElJuego",
        "featured_games": featured_games,
        "top_news": top_news,
        "news": news,
        "launch_games": launch_games,
        "video": video,
        "videos": videos
    }
    return render(request, "games/index.html", context)


def game_detail(request, slug=None):
    instance = get_object_or_404(Game, slug=slug)
    context = {
        "title": "",
        "instance": instance
    }
    return render(request, "games/detail.html", context)


def news_detail(request, slug=None):
    instance = get_object_or_404(News, slug=slug)
    context = {
        "title": "",
        "instance": instance
    }
    return render(request, "games/news_detail.html", context)
