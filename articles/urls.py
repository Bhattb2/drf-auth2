from django.urls import path

from .views import ArticleDetail, ArticleList

urlpatterns = [
    path('<int:pk>/', ArticleDetail.as_view()),
    path('', ArticleList.as_view()),
]