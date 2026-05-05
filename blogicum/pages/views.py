from django.shortcuts import render

def about(request):
    template = 'pages/about'
    return render(request, template)

def rules(request):
    template = 'pages/rules'
    return render(request, template)
