from django.urls import path
from app.views import *
app_name='something'
urlpatterns=[
    path('temfirst/',temfirst,name='temfirst'),
    path('temsecond/',temsecond,name='temsecond'),
]
