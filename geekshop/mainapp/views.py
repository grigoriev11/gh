from django.shortcuts import render

render(request, 'mainapp/index.html', content)


def main(request):
    return render(request, 'mainapp/index.html')
    

def products(request):
    return render(request, 'mainapp/products.html')
    

def contact(request):
    return render(request, 'mainapp/contact.html')


# Create your views here.
