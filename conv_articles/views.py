from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Article, Vente, Approvisionnement
from .serializers import ArticleSerializer, VenteSerializer, ApprovisionnementSerializer
from rest_framework import permissions

# Create your views here.


class ArticleViewSet(ModelViewSet):
	serializer_class = ArticleSerializer
	queryset = Article.objects.all()
	permission_classes = [permissions.AllowAny]


class VenteViewSet(ModelViewSet):
	serializer_class = VenteSerializer
	queryset = Vente.objects.all()
	permission_classes = [permissions.AllowAny]


class ApprovisionnementViewSet(ModelViewSet):
	serializer_class = ApprovisionnementSerializer
	queryset = Approvisionnement.objects.all()
	permission_classes = [permissions.AllowAny]