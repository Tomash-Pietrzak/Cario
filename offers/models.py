from django.db import models
from cario import settings


class Offer(models.Model):
    Petrol = "BENZYNA"
    LPG = "LPG"
    Diesel = "DIESEL"
    Electric = "ELEKTRYCZNY"
    Hybrid = "HYBRYDA"
    Fuel_Choices = (
        (Petrol, "Benzyna"), (LPG, "LPG"), (Diesel, "Diesel"), (Electric, "Elektryczny"), (Hybrid, "Hybryda"))

    Auto = "AUTOMATYCZNA"
    Manu = "MANUALNA"

    Tran_Choices = ((Manu, "Manualna"), (Auto, "Automatyczna"))
    fuel = models.TextField(max_length=25, choices=Fuel_Choices, default=Petrol)
    power = models.IntegerField()
    mileage = models.IntegerField()
    transmission = models.TextField(max_length=25, choices=Tran_Choices, default=Manu)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    brand = models.TextField(max_length=25, default='')
    model = models.TextField(max_length=25, default='')
    price = models.IntegerField()

    class Meta:
        ordering = ['brand']

    def __str__(self):
        return self.mark, self.model, self.owner
