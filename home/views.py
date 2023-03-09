from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def members_grp(request):
    return render(request, 'members.html')