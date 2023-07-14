from django import forms
from app.models import *

class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        help_texts={'topic_name':'<i>Should not be integers</i>'}

class WebpageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        fields=['topic_name','name']
        labels={'name':'Name of the Player'}


class AccessrecordsModelForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        #fields='__all__'
        exclude=['author']
        widgets={'date':forms.DateInput}
