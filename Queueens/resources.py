from import_export import resources
from .models import Inscrito

class InscritoResource(resources.ModelResource):
    class Meta:
        model = Inscrito