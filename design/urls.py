from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.homepage, name='Home'),
    path('contact/', views.contacts, name="contact"),
    # path('sendmail/', views.sendmail, name="sendmail"),
    path('professional/',views.professionalpage, name='Professional'),
    path('about/',views.aboutpage, name='About'),
    path('proprofile/',views.ProProfile, name='proprofile'),
    path('roomDesign.html', views.RoomDesign , name='Room Design'),
    path('plantsAtoZ.html', views.PlantsAtoZ,name='plants a to z'),
    path('decorating.html', views.Decorating,name='Decorate'),
    path('designStyle.html', views.Designing,name='Style'),
    path('smallSpace.html', views.Small,name='Space'),
    path('outDoor.html', views.Out,name='OUT'),
    path('inDoor.html', views.Ind,name='IN'),
    path('skills.html', views.Skl,name='Skill'),
    path('clen.html', views.Cln,name='Clean'),
    path('addDesign.html', views.AddDesign,name='add design'),
    path('addDesign', views.AddDesign,name='add design'),
    path('myDesign', views.MYDesign,name='mydesign'),
    path('mydesign.html', views.MYDesign,name='mydesign1'),
    
]

#from django.urls import path
#from .views import *
#from django.conf.urls.static import static
#from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#urlpatterns = [
    #path('roomDesign.html', RoomDesign , name='Room Design'),
    #path('plantsAtoZ.html', PlantsAtoZ,name='plants a to z'),
    #path('decorating.html', Decorating,name='Decorate'),
    #path('addDesign.html', AddDesign,name='add design'),
    #path('addDesign', AddDesign,name='add design'),
    # path('login/', login_page , name='login_page'),
    # path('register/', register_page , name='register_page'),

#]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()