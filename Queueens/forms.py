from django import forms
from .models import Inscrito

class QOTSAForm(forms.ModelForm):

	class Meta:
		model = Inscrito
		fields = ('nombre', 'apellido', 'correo', 'celular',)