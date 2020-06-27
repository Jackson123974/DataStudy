from django import  forms
from data import models
class BootstrapForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BootstrapForm,self).__init__(*args,**kwargs)
        for k, v in self.fields.items():
            v.widget.attrs['class'] = 'form-control'