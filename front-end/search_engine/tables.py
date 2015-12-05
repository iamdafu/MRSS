import django_tables2 as tables
from .models import SearchWord, Recommendation

class RecommendationTable(tables.Table):
    # search_word = tables.Column(verbose_name = "sym")
    class Meta:
        model = Recommendation
        attrs = {"class": "paleblue"}
