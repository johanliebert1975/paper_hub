from django.shortcuts import render,redirect
from .forms import QuestionPaperForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def tab1(request):
    return render(request, 'tab1.html')

def tab2(request):
    return render(request, 'tab2.html')

def tab3(request):
    return render(request, 'tab3.html')

def upload_paper(request):
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to homepage or wherever
    else:
        form = QuestionPaperForm()
    return render(request, 'upload.html', {'form': form})