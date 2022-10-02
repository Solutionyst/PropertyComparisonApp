from django.db import models

class propertyData(models.Model):
    dateFound = models.DateField()
    propertyID = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    roadName = models.CharField(max_length=100)
    jerseyArea = models.CharField(max_length=100)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    parking = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Found: {} - PropertyID: {}".format(self.dateFound, self.propertyID)


class DailyData(models.Model):
    date = models.DateField()
    Parish = models.CharField(max_length=100)
    Average = models.IntegerField()

    def __str__(self):
        return "{} on {}".format(self.Parish, self.date)