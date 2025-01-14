from django.urls import path
from .import views
urlpatterns=[
    path('',views.landingpage, name='home'),
    path('about/',views.aboutfunc,name='about' ),
    path('news/',views.newsfun,name='news' ),
    path('contact/',views.contactfun,name='contact' ),
    
]