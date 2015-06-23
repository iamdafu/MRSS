from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from .models import SearchWord, Recommendation
from .forms import SearchWordForm

def index(request):
    return render(request, 'search_engine/index.html', {'form': SearchWordForm()})

def get_recommendation(request):
    if request.method == "POST":
        form = SearchWordForm(request.POST)
        if form.is_valid():
            symptom = form.cleaned_data['search_word']
            search_symptom = SearchWord.objects.get(search_word_text=symptom)

            # return HttpResponseRedirect("search_engine/results.html")
            return render(request, "search_engine/results.html",
                    { "recommendation":
                        Recommendation.objects.filter(search_word=search_symptom)})
    else:
        form = SearchWordForm()

    return render(request, "search_engine/index.html", {"form": form})

def results(request, search_word):
    return HttpResponse("You're searching word %s." % search_word)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
