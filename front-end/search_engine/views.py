from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from .models import SearchWord
from .forms import SearchWordForm

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'search_engine/index.html', {'form': SearchWordForm()})

def results(request, search_word):
    return HttpResponse("You're searching word %s." % search_word)

def get_recommendation(request):
    if request.method == "POST":
        form = SearchWordForm(request.POST)
        if form.is_valid():
            # pass

            return HttpResponseRedirect("search_engine/results.html")
    else:
        form = SearchWordForm()

    return render(request, "search_engine/index.html", {"form": form})

