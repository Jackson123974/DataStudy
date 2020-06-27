from django import  forms
from data  import models
from . import base
class TieModelForm(base.BootstrapForm):
    class Meta:
        model = models.Tieba
        fields = "__all__"