from django import forms

from newsletters.models import Join


class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = [
            "email",
        ]
