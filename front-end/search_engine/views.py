from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from .models import SearchWord
from .forms import SearchWordForm

def index(request):
    return render(request, 'search_engine/index.html', {'form': SearchWordForm()})

def get_recommendation(request):
    if request.method == "POST":
        form = SearchWordForm(request.POST)
        if form.is_valid():
            search_word = form.cleaned_data['search_word']

            # return HttpResponseRedirect("search_engine/results.html")
            return render(request, "search_engine/results.html",
                    {"search_word": search_word})
    else:
        form = SearchWordForm()

    return render(request, "search_engine/index.html", {"form": form,
        "search_word": search_word})

def results(request, search_word):
    return HttpResponse("You're searching word %s." % search_word)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
