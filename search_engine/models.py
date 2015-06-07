from django.db import models

# Create your models here.

import datetime

class User(models.Model):
# leave it to the future
    pass

    # user_name = models.CharField(max_length=20)
    # email = models.CharField(max_length=20)
    # phone_number = models.CharField(max_length=15)

class SearchWord(models.Model):
    search_word_text = models.CharField(max_length=200)
    search_date = models.DateField("search date", default=datetime.date.today)

    def __unicode__(self):
        return self.search_word_text

class Recommendation(models.Model):
    search_word = models.ForeignKey(SearchWord)
    recommendation_text = models.CharField(max_length=200)
    rank = models.IntegerField()

    def __unicode__(self):
        return self.recommendation_text

class SourceUrl(models.Model):
    recommendation = models.ForeignKey(Recommendation)
    source_url = models.CharField(max_length=200)
    pub_date = models.DateField("search date")
    location = models.CharField(max_length=200)

    def __unicode__(self):
        return self.source_url
