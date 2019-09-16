from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Appartment(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, help_text="Rue et n° de rue")
    city = models.CharField(max_length=50, help_text="Ville")
    zipcode = models.CharField(max_length=10, help_text="Code postal")
    price = models.IntegerField(default=0, help_text="Prix à la journée en €")
    cover_picture = models.ImageField(null=True, help_text="Photo de couverture de l'appartement")
    nb_bedrooms = models.IntegerField(default=0, help_text="Nombre de chambres")
    nb_bathrooms = models.IntegerField(default=0, help_text="Nombre de salles de bains")
    surface = models.IntegerField(default=0, help_text="Surface en m2")
    description = models.TextField(help_text="Description de l'appartement")
    is_visible = models.BooleanField(default=False, help_text="Cocher pour rendre l'appartement publiquement visible")
    is_bookable = models.BooleanField(default=False,
                                      help_text="Cocher pour que n'importe qui puisse faire une demande de réservation")

    slug = models.SlugField(max_length=255, editable=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def full_address(self):
        return "{} {} {}".format(self.address, self.city, self.zipcode)


class AppartmentImage(models.Model):
    image = models.ImageField()
    apparment = models.ForeignKey(Appartment, null=True, on_delete=models.SET_NULL, related_name='images')

    def __str__(self):
        return self.image.name


class Reservation(models.Model):
    STATUS_CHOICES = (
        ('waiting', 'Waiting approval'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    )

    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    status = models.CharField(choices=STATUS_CHOICES, default="waiting", max_length=20)
    appartment = models.ForeignKey(Appartment, null=True, on_delete=models.SET_NULL)

    created_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name='Date de création'
    )
    modified_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Date de dernière modification'
    )


    def __str__(self):
        return "Réservation de {} pour un total de {} à {}".format(self.name, self.start_date, self.end_date)

    def total_price(self):
        days = (self.end_date - self.start_date).days

        return days * self.appartment.price
