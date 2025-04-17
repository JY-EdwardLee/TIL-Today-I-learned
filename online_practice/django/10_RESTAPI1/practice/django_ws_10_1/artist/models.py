from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField(max_length=100)
    agency = models.TextField()
    debut_data = models.DateField(auto_now_add=True)
    is_group = models.BooleanField()

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Artist_detail", kwargs={"pk": self.pk})
