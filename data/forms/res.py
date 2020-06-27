from django import  forms
from data  import models
from . import base
class ResModelForm(base.BootstrapForm):
    class Meta:
        model = models.Result
        fields = "__all__"