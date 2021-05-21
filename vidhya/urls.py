from  rest_framework.routers import SimpleRouter
from vidhya.views import MyOwnMixin
simple=SimpleRouter()
simple.register('api/v1',MyOwnMixin)

urlpatterns=simple.urls