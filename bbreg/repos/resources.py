from tastypie.authorization import Authorization
#from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from models import Repositorio


class RepositoryResource(ModelResource):
    class Meta:
        queryset = Repositorio.objects.all()
        resource_name = 'repositorios'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()
