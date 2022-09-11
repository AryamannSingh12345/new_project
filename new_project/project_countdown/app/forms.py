from django import forms

class answer(forms.Form):
    your_answer = forms.CharField(widget = forms.Textarea(attrs = {'rows' : 5, 'size': 40,  'style': 'border-color:darkgoldenrod; border-radius: 10px;'}))

class large_numbers(forms.Form):
    enter_the_number_of_large_numbers = forms.IntegerField(widget = forms.TextInput(attrs = {'rows' : 10, 'size' : 25, 'style': 'border-color:darkgoldenrod; border-radius: 10px;'}))

class team_number(forms.Form):
    Team_number = forms.IntegerField(widget = forms.TextInput(attrs = {'rows' : 10, 'size' : 45, 'style': 'border-color:darkgoldenrod; border-radius: 10px;'}))
