from rest_framework.serializers import ModelSerializer
from .models import Article, Vente, Approvisionnement

class ArticleSerializer(ModelSerializer):

	class Meta:
		model = Article
		fields = '__all__'
		ref_name = 'Articles_articles'

class VenteSerializer(ModelSerializer):

	class Meta:
		model = Vente
		fields = '__all__'#["nom","quantite_achat"]
		ref_name = 'vente_articles'

class ApprovisionnementSerializer(ModelSerializer):

	class Meta:
		model = Approvisionnement
		fields = '__all__'
		ref_name = 'approvisionnement_articles'