from django.shortcuts import render
from unicodedata import category

from news_app.models import News, NewsCategory

# Create your views here.
# Функция для показа всех новостей на главном экране
def home(request):
    all_news = News.objects.all()
    all_category = NewsCategory.objects.all()
    return render(request, "index.html", context={"all_news": all_news,
                                                  "all_category": all_category})


# Функция для показа определенной новости
def get_exact_news(request, pk):
    exact_news = News.objects.filter(id=pk).first()
    # News()
    return render(request, "exact_news.html", context={"exact_news": exact_news})

def all_categories_pk(request, pk):
    all_categories = News.objects.filter(cotegory=pk).all()
    print(all_categories)
    return render(request, 'category.html', context={"all_categories": all_categories})