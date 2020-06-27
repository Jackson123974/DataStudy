from django import  forms
from data  import models
from . import base
class NewModelForm(base.BootstrapForm):
    class Meta:
        model = models.News
        fields = "__all__"