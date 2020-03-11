from django.shortcuts import render, get_object_or_404

def homepage_view(request):
    return render(request, 'home/base.html')