from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as  dt
from .models import Articles

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def convert_dates(dates):
	#Function that gets the weekdat number for the date.
	day_number = dt.date.weekday(dates)
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
	#Returning the actual day of the week
	day = days[day_number]
	return day


def news_of_day(request):
    date = dt.date.today()

    day=convert_dates(date)
    news =Articles.todays_news()
    return render(request,'all-news/today-news.html',{"date":date,"news":news})


def past_days_news(request,past_date):
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.data.today():
        return redirect(news_of_day)


    news = Articles.days_news(date) 
    return render(request, 'all-news/past-news.html',{"date": date , "news":news })
def search_results(request):

    if  'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Articles.search_by_title(search_term)
        message = f"{ search_term }"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})


def article(request,article_id):
    try:
        article = Articles.objects.get(id =article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html",{"article":article})