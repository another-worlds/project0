from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=48)
    text = models.TextField()
    pub_date = models.DateTimeField('Date published', auto_now=True)
    score = models.IntegerField(default=0)
    
    def to_str(self):
        return f"Post titled '{self.title} published on {self.pub_date} with {self.score} score"

class Comment(models.Model):
    author = models.CharField(max_length=48)
    text = models.TextField()
    pub_date = models.DateTimeField("Date published", auto_now=True)
    score = models.IntegerField(default = 0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def to_str(self):
        return f"Comment to the {self.post} post by {self.author} published on {self.pub_date} with {self.score}"