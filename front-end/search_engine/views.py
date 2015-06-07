from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from .models import SearchWord
from .forms import SearchWordForm
from .forms import ContactForm

def index(request):
    # template = loader.get_template('search_engine/index.html')
    # context = RequestContext(requese, 
    # return HttpResponse("Hello, test")
    return render_to_response('search_engine/index.html')

def results(request, search_word):
    return HttpResponse("You're searching word %s." % search_word)

def get_search_word(request):
    if request.method == "POST":
        form = SearchWordForm(request.POST)
        if form.is_valid():
            # pass

            return HttpResponseRedirect("search_engine/results.html")
    else:
        form = SearchWordForm()

    return render(request, "search_engine/index.html", {"form": form})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def search_form(request):
    return render(reques, 'search_engine/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})


