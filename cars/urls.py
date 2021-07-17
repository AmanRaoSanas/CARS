from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('register', views.register, name='register'),
    path('forget', views.forget, name='forget'),
    path('signing_in', views.signing_in, name='signing_in'),
    path('register_in', views.register_in, name='register_in'),
    path('forget_in', views.forget_in, name='forget_in'),
    path('search', views.search, name='search'),
    path('search_in', views.search_in, name='search_in'),
    path('help', views.help, name='help'),
    path('feedback', views.feedback, name='feedback'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('hatchback', views.hatchback, name='hatchback'),
    path('sedan', views.sedan, name='sedan'),
    path('mpv', views.mpv, name='mpv'),
    path('muv', views.muv, name='muv'),
    path('suv', views.suv, name='suv'),
    path('amt', views.amt, name='amt'),
    path('cvt', views.cvt, name='cvt'),
    path('auto', views.auto, name='auto'),
    path('crossover', views.crossover, name='crossover'),
    path('crossover', views.crossover, name='crossover'),

    path('demo', views.demo, name='demo'),
]

