from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

feira_view_basic_actions = FeiraViewSet.as_view({
    'get': 'get_all_feira',
    'post': 'create_feira',
    'put': 'update_feira',
    'delete': 'delete_feira',
})


get_feira_by_distrito_actions= FeiraViewSet.as_view({
    'get': 'get_feira_by_distrito',
})

get_feira_by_regiao5_actions= FeiraViewSet.as_view({
    'get': 'get_feira_by_regiao5',
})

get_feira_by_nome_feira_actions= FeiraViewSet.as_view({
    'get': 'get_feira_by_nome_feira',
})

get_feira_by_bairro_actions= FeiraViewSet.as_view({
    'get': 'get_feira_by_bairro',
})

urlpatterns = [
    path('feiras/', feira_view_basic_actions, name='get_all_feira'),
    path('feiras/feira/', feira_view_basic_actions, name='create_feira'),
    path('feiras/<id>', feira_view_basic_actions, name='update_feira'),
    path('feiras/<id>', feira_view_basic_actions, name='delete_feira'),
    path('feiras/feira/distrito/<distrito>/', get_feira_by_distrito_actions, name='get_feira_by_distrito'),
    path('feiras/feira/regiao5/<regiao5>/', get_feira_by_regiao5_actions, name='get_feira_by_regiao5'),
    path('feiras/feira/nome_feira/<nome_feira>/', get_feira_by_nome_feira_actions, name='get_feira_by_nome_feira'),
    path('feiras/feira/bairro/<bairro>/', get_feira_by_bairro_actions, name='get_feira_by_bairro')
]