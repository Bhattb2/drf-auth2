from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Article
from .permissions import IsAuthorOrReadOnly
from .serializer import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer