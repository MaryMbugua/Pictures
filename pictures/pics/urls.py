from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^search$',views.search,name='search'),
    url(r'^locations/$',views.places,name='places'),
    url(r'^locations/naivasha$',views.naivasha,name='naivasha'),
    url(r'^locations/nairobi$',views.nairobi,name='nairobi'),
    url(r'^locations/kitale$',views.kitale,name='kitale'),
    url(r'^locations/kisumu$',views.kisumu,name='kisumu'),
    url(r'^locations/watamu$',views.watamu,name='watamu'),
    url(r'^locations/nyeri$',views.nyeri,name='nyeri'),
    
   ]
