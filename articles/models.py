from django.db import models

# Create your models here.
class Article (models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add =True)
    #add in thumbnail

    def __str__(self):
        return self.title
    # print "hello"

    def snippet(self):
        return self.body[:50] + "..."
#migration file
#python manage.py makemigrations
#python manage.py migrate


#Didn't quite work
