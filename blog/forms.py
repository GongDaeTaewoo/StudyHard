from django import forms

from blog.models import Study, Reference, Memo


class StudyPostForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = "__all__"


class ReferPostForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"


class MemoPostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = "__all__"
