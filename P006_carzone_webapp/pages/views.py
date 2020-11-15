from django.shortcuts import render

# Create your views here.

# Create a function to retrieve view from template (html) folder under pages
def home(request):
    return render(request, 'pages/home.html')
