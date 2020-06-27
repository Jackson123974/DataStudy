from django import  forms
from data  import models
from . import base
class MatchModelForm(base.BootstrapForm):
    class Meta:
        model = models.Match
        fields = "__all__"