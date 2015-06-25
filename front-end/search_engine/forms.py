from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

class SearchWordForm(forms.Form):
    search_word = forms.CharField(
            label = "search word",
            max_length = 200,
            required = True,
            widget = forms.TextInput(attrs={'placeholder':"Please input some symptom ..."}),
            )

    def __init__(self, *args, **kwargs):
        super(SearchWordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'searchWordFormId'
        self.helper.form_method = 'get'
        self.helper.form_action = '/search_engine/get_recommendation/'
        # self.helper.form_action = '/search_engine/results/'
        self.helper.layout = Layout(
            # Field('search_word', placeholder="Please ..."),
            FieldWithButtons('search_word', StrictButton('<span class="glyphicon glyphicon-search"></span>', type='submit', css_class='btn-default')),
        )
        self.helper.form_show_labels = False
