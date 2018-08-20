from django.db import models


class Test(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey('auth.User', related_name='tests', on_delete=models.CASCADE)
    client_number = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        ordering = ('created_at',)


class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    test = models.ForeignKey(Test, related_name='items', on_delete=models.CASCADE)
    number = models.CharField(max_length=16)
    score = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        ordering = ('created_at',)
