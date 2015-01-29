__author__ = 'piratos'
from .models import Report, report_status
from django import forms


class ReportFrom(forms.ModelForm):
    status = forms.CharField(max_length=128,
                             widget=forms.HiddenInput(),
                             initial='pending approval',
                             )
    votes = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Report