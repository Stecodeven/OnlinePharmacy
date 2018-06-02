from django import forms


class Search(forms.Form):
    content = forms.CharField(label='搜索', max_length=20)
