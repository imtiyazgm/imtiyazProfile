from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.homePage, name='homepage'),
    path('workExp_npkfze/', views.workExp, name='workExp_npkfze'),
    path('workExp_npkfzco/', views.workExpfzco, name='workExp_npkfzco'),
    path('workExp_Midco/', views.workExpMidco, name='workExp_Midco'),
    path('workExp_Alma/', views.workExpAlma, name='workExp_Alma'),

    
]
