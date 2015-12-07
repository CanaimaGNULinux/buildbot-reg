from tastypie.api import Api
from resources import RepositoryResource

api_01 = Api(api_name='0.1')
api_01.register(RepositoryResource())