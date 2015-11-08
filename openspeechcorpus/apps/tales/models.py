from django.db import models

from openspeechcorpus.apps.core.models import AudioData
# Create your models here.

class Style(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    starts = models.DateField(blank=True, null=True)
    ends = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    death = models.DateField(blank=True, null=True)
    styles = models.ManyToManyField(Style, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Tale(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.title


class TaleSentence(models.Model):
    tale = models.ForeignKey(Tale)
    place = models.IntegerField(blank=True, null=True)
    text = models.TextField()

    def __unicode__(self):
        return unicode(self.id) + " " + unicode(self.tale) + " " + unicode(self.place)


class SentenceTaleSpeech(models.Model):
    tale_sentence = models.ForeignKey(TaleSentence)
    audio = models.ForeignKey(AudioData)







