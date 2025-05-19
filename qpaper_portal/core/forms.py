from django import forms
from .models import QuestionPaper

#connecting the question paper model built 
class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['name', 'details', 'source', 'pdf']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 3}),
        }
