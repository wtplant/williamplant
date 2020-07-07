from django.shortcuts import render

def home_view(request, *args,**kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"index.html", {})

def about_v(request, *args,**kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html", {})

def contact_v(request, *args,**kwargs):
    return render(request,"contact.html", {})
   