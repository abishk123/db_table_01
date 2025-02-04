from django import forms
from app.models import *

# DJANGO FORMS
class TopicForm(forms.Form):
    topic_name = forms.CharField(label='Topic', max_length=100)

class WebpageForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    url = forms.URLField(label='URL')
    topic_name = forms.ModelChoiceField(label='Topic',queryset=Topic.objects.all())
    email = forms.EmailField(label='Email')

class AccessRecordsForm(forms.Form):
    name = forms.ModelChoiceField(label='webpage object', queryset=Webpage.objects.all())
    date = forms.DateField(label='Date')
    author = forms.CharField(label='Author', max_length=100)




# MODEL FORMS
class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        labels={'topic_name':'TOPIC_NAME'}

class WebpageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class AccessRecordsModelForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
