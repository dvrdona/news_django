from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=256)



# News
# title
# main_text
# date
class News(models.Model):
    title = models.CharField(max_length=128)
    main_text = models.TextField(max_length=256)
    data = models.DateTimeField(auto_now_add=True)
    cotegory = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

