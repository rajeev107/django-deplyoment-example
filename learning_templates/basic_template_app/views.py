from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'name':'Hello Filter','Number':540}
    return render(request,'basic_template_app/index.html',context_dict)

def other(request):
    return render(request,'basic_template_app/other.html')

def relative(request):
    return render(request,'basic_template_app/relative_template_url.html')
