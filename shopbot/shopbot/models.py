from django.db import models


class ShopBot(models.Model):
	userid = models.CharField(max_length=200)

	def __unicode__(self):
		return self.userid # User Identity network



class ShopBotDatabase(models.Model):
	userid = models.ForeignKey(ShopBot)
	product = models.CharField(max_length=100)
	product_desc = models.CharField(max_length=300)

	def __unicode__(self):
		return "Product for " + str(self.userid.userid) # User Identity