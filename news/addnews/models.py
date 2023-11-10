from django.db import models

# Create your models here.
class Category(models.Model):
    category =models.CharField(max_length=25)
class News(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='news_category')
    news_name = models.CharField(max_length=25,null=False,blank=False)
    picture = models.ImageField()
    post_by = models.CharField(max_length=25)
    post = models.DateField(auto_now=True)

