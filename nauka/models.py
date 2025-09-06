from django.db import models

class Lista(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class Slowko(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='slowka')
    angielski = models.CharField(max_length=100)
    polski = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.angielski} – {self.polski}"