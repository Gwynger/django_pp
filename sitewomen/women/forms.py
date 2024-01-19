from django import forms
from django.core.exceptions import ValidationError
from .models import Women


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tag']
        labels = {
            'slug': 'URL',
            'tag': 'Tags',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Longer than 50 characters')

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='File')

