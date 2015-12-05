from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django_tables2 import RequestConfig

from .models import SearchWord, Recommendation
from .forms import SearchWordForm
from .tables import RecommendationTable

def index(request):
    return render(request, 'search_engine/index.html', {'form': SearchWordForm()})

def get_recommendation(request):
    if request.method == "GET":
        form = SearchWordForm(request.GET)
        if form.is_valid():
            symptom = form.cleaned_data['search_word']
            search_symptom = SearchWord.objects.filter(search_word_text=symptom)
            # if search_symptom:
            #     recommendation = Recommendation.objects.filter(search_word=search_symptom)

            #     return render(request, "search_engine/results.html",
            #             { "recommendation": recommendation})
            # else:
            #     return render(request, "search_engine/index.html", {"form": form})
            table = RecommendationTable(Recommendation.objects.filter(search_word=search_symptom))
            RequestConfig(request).configure(table)

            return render(request, "search_engine/results.html",
                    { "table": table})
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
