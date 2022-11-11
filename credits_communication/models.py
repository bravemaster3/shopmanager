from django.db import models
from django.utils import timezone
import uuid
from django.core.validators import MinValueValidator

# Create your models here.
class Article(models.Model):
	id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
	nom = models.CharField(unique=True, max_length=100, db_index=True, help_text="Entrer le nom de l'article")
	description = models.TextField(help_text="Rajouter des descriptions supplémentaires, ex. volume de la boite")
	prix_achat = models.DecimalField(max_digits=10, decimal_places=4, default=20000.0)
	prix_vente = models.DecimalField(max_digits=10, decimal_places=4, default=21000.0)
	devise = models.CharField(max_length=30, default="FCFA")
	quantite = models.PositiveIntegerField()

	class Meta:
		ordering = ('nom',)

	def __str__(self):
		return self.nom


class Approvisionnement(models.Model):
	id = models.CharField(primary_key = True, unique=True, max_length=100, db_index=True, editable=False, help_text="Entrer l'approvisionnement", default=uuid.uuid4)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	quantite_approvision = models.PositiveIntegerField()
	date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		try:#if self.pk:
			old_quantity = self.__class__.objects.get(pk=self.pk).quantite_approvision
			instance_exists = True

		except:#if not self.pk:
			instance_exists = False
			

		super(Approvisionnement, self).save(*args, **kwargs)

		if instance_exists == False:
			self.article.quantite += self.quantite_approvision
		if instance_exists == True:
			diff_quantity = self.quantite_approvision - old_quantity
			self.article.quantite += diff_quantity

		#super(Approvisionnement, self).save(*args, **kwargs)
		self.article.save()


class Vente(models.Model):
	id = models.CharField(primary_key = True, unique=True, max_length=100, db_index=True, editable=False, help_text="Entrer la vente", default=uuid.uuid4)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	quantite_vente = models.PositiveIntegerField()
	benefice = models.CharField(max_length=30, editable=False)
	date = models.DateTimeField(auto_now_add=True)

	# def total(self, *args, **kwargs):
	# 	#super(Vente, self)
	# 	result = self.article.prix_unit * self.quantite_vente
	# 	return result

	def calculer_benefice(self, *args, **kwargs):
		result = self.quantite_vente * (self.article.prix_vente - self.article.prix_achat)/self.article.prix_vente
		return result


	def save(self, *args, **kwargs):

		try:#if self.pk:
			old_quantity = self.__class__.objects.get(pk=self.pk).quantite_vente
			instance_exists = True

		except:#if not self.pk:
			instance_exists = False
			

		#super(Vente, self).save(*args, **kwargs)

		if instance_exists == False:
			self.article.quantite -= self.quantite_vente
		if instance_exists == True:
			diff_quantity = self.quantite_vente - old_quantity
			self.article.quantite -= diff_quantity

		self.article.save()

		self.benefice = self.calculer_benefice()
		super(Vente, self).save(*args, **kwargs)
