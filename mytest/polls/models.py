from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'Question with text "{self.question_text}" posted on {self.pub_date}'
    
    def pubslihed_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1) 
    
class Choice(models.Model):
    choice_text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Choice with text "{self.choice_text}" with {self.votes} score'
    