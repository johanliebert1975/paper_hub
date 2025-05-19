from django.db import models

  
class QuestionPaper(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    source = models.CharField(max_length=200, blank=True)
    pdf = models.FileField(upload_to='question_papers/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name