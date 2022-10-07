from django import forms
from bootstrap_typeahead.widgets import TypeaheadInput

class StateForm(forms.Form):
    query = forms.CharField(
        widget=TypeaheadInput(
            options={
              'hint': True,
              'highlight': True,
              'minLength': 1
            },
            datasets={
              'name': 'states',
              'source': 'substringMatcher(states)',
            }
        )
    )