from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, 'landingpage.html')
def aboutfunc(request):
    return render(request, 'about.html')
def newsfun(request):
    return render(request, 'news.html')
def contactfun(request):
    return render(request, 'contact.html')
