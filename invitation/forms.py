from django import forms
from invitation.models import InvitationRequest


class InvitationKeyForm(forms.Form):
    email = forms.EmailField()


class InvitationRequestForm(forms.ModelForm):
    class Meta:
        model = InvitationRequest
