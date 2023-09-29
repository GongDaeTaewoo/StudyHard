from django.urls import path

from blog import views

app_name='blog'
urlpatterns = [

    # study
    path('', views.home),
    path('study/', views.study_list, name="study-list"),
    path('study/<int:pk>/', views.study_detail, name="study-detail"),
    path('study/create/', views.study_create, name="study-create"),
    path('study/<int:pk>/update/', views.study_update, name="study-update"),
    path('study/<int:pk>/delete/', views.study_delete, name="study_delete"),
    #
    # # reference
    path('refer/', views.refer_list, name="refer-list"),
    path('refer/<int:pk>/', views.refer_detail, name="refer-list"),
    path('refer/<int:pk>/delete/', views.refer_delete, name="refer-delete"),
    path('refer/create/', views.refer_create, name="refer-create"),
    #
    # # memo
    path('memo/', views.memo_list, name="memo-list"),
    path('memo/<int:pk>/delete/', views.memo_delete, name="memo-delete"),
    path('memo/create/', views.memo_create, name="memo-create"),
]
