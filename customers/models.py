from django.db import models
from typing import Any

class Customer(models.Model):
    """
    Model representing a Customer (Company).
    """
    name = models.CharField(max_length=255)
    vat_id = models.CharField(max_length=20)  # OIB
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Overrides the save method to include any custom logic.
        """
        super().save(*args, **kwargs)

    @classmethod
    def get_all(cls):
        """
        Retrieves all Customer instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Customer objects.
        """
        return cls.objects.all()
