from django import forms

from blog.models import Study, Reference, Memo


class StudyPostForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['title','subject','content','level','importance']


class ReferPostForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['title','subject','address']


class MemoPostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title','content']
