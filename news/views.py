from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Articles, NewsLetterRecipients
from .forms import NewsLetterForm, NewArticleForm
# from .email import send_welcome_email
from .email import send_welcome_email


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def convert_dates(dates):
    # Function that gets the weekdat number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', "Sunday"]
    # Returning the actual day of the week
    day = days[day_number]
    return day


def news_of_day(request):
    date = dt.date.today()
    news = Articles.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if request.method == 'POST':
            form = NewsLetterForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['your_name']
                email = form.cleaned_data['email']
                recipient = NewsLetterRecipients(name=name, email=email)
                recipient.save()
                send_welcome_email(name, email)

                HttpResponseRedirect('news_of_day')
    else:
        form = NewsLetterForm()

    return render(request, 'all-news/today-news.html', {"date": date, "news": news, "letterForm": form})


def past_days_news(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.data.today():
        return redirect(news_of_day)

    news = Articles.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news": news})


def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Articles.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html', {"message": message, "articles": searched_articles})


@login_required(login_url='/accounts/login/')
def article(request, article_id):
    try:
        article = Articles.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-news/article.html", {"article": article})


@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('newsToday')

    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form}) 
