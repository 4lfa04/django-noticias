from django.forms import ModelForm
from .models import Noticia

class NoticeForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['title','description', 'image']