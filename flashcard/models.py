from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class FlashCard(models.Model):
    name_pl = models.CharField(max_length=255, null=True, blank=True)
    name_eng = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="flashcards")
    tag = models.ManyToManyField("tags.Tag")


