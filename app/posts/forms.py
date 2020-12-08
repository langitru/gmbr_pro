from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Posts
from django.utils.translation import gettext_lazy as _

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'anons', 'full_text', 'date_public']
        localized_fields = ('date_public',)
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Название поста'
                }
            ),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс  поста'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание поста'
            }),
            'date_public': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
                'type': 'date',
                
            }),
            
        }


# from django import forms
# from .models import Posts
# from django.utils import timezone

# class PostsForm(forms.Form):
#     title = forms.CharField( max_length=180)
#     anons = forms.CharField( max_length=255 )
#     full_text = forms.CharField(widget=forms.Textarea)
#     date_public = forms.DateTimeField(default=timezone.now )

#     # class Meta:
#     #     model = Posts
#     #     fields = ['title', 'anons', 'full_text', 'date_public']

#     #     widgets = {
#     #         'title': TextInput(attrs={
#     #             'class': 'form-control',
#     #             'placeholder': 'Название поста'
#     #         }),
#     #         'anons': TextInput(attrs={
#     #             'class': 'form-control',
#     #             'placeholder': 'Анонс  поста'
#     #         }),
#     #         'full_text': Textarea(attrs={
#     #             'class': 'form-control',
#     #             'placeholder': 'Содержание поста'
#     #         }),
#     #         'date_public': DateTimeInput(attrs={
#     #             'class': 'form-control',
#     #             'placeholder': 'Дата публикации',
#     #             'type': 'date',
#     #         }),
            
#     #     }