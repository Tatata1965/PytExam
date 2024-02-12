from django.shortcuts import render

# Create your views here.
def tata(request):
    return render(request, 'kuk.html')


def index(request):
    return render(request, 'index.html', {'name': ['Tatyana', 'Igor', 'Sasha']})

def kachan(request):
    return render(request, 'each.html')


def some_url(request,s):
    if s == '223':
        return render(request, 'index.html',{'native':'Django'})
    if s == '222':
        return render(request, 'each.html', {'native':['С','C++','С#','Java']})
    if s == '221':
        return render(request, 'kuk.html', {'native':'Python'})
    if s == '220':
        return render(request, 'fon.html')

    return render(request, 'error.html', {'url': s})