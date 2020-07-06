from django.db import models



class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.CharField(max_length=120)
	manager = models.CharField(max_length = 60)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


event1 = Event(name="blmxsTest Evedggggggerernt5", event_date="2018-12-17",
venue="test venue", manager="s")


event1.save()


##	tx_id = models.CharField('tx_id', max_length=120)
##	tx_date = models.DateTimeField('tx_date')
	##tx_amount = models.DecimalField('tx_amount', max_digits=5, decimal_places=2)




##event5 = crypto_load(tx_id="999994545345", tx_date="2020-12-17")


##event5.save()

 