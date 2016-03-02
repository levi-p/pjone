from django.conf.urls import * #url
from . import views

urlpatterns = patterns('',
    url(r'^home/',views.show_product)
    )
