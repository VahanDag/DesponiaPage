from django.shortcuts import render

def error404(request, exception):
    return render(request, "errors/404.html")

def error403(request, exception):
    return render(request, "errors/403.html")

def error400(request, exception):
    return render(request, "errors/400.html")

def error500(request, *args, **argv):
    return render(request, '500.html', status=500)

