from django.shortcuts import render

# Create your views here.
def error404(request,exception):
    return render(request,'Error/404.html')

def error500(request):
    return render(request,'Error/500.html')


