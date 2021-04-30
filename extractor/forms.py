from django import forms
from extractor.serializers.serializers import ExtractorSerializer

METHOD_CHOICES = ExtractorSerializer.METHODS

class RequestForm(forms.Form):
    text = forms.CharField(label='Text')
    method = forms.ChoiceField(choices=METHOD_CHOICES, required=True)
    num_of_keywords = forms.IntegerField()
