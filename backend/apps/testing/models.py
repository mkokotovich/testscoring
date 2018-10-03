from django.db import models


class Test(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey('auth.User', related_name='tests', on_delete=models.CASCADE)
    client_number = models.DecimalField(max_digits=8, decimal_places=0)

    CBCL_6_18 = 'cbcl_6_18'
    CBCL_1_5 = 'cbcl_1_5'
    CONNERS3_PARENT = 'conners3_parent'
    CONNERS3_SELF = 'conners3_self'
    TSCYC = 'tscyc'
    BRIEF2 = 'brief2'
    SRS2 = 'srs2'
    SCARED = 'scared'
    TSCC = 'tscc'
    TEST_TYPE_CHOICES = (
        (CBCL_6_18, 'CBCL 6-18'),
        (CBCL_1_5, 'CBCL 1.5-5'),
        (CONNERS3_PARENT, 'Conners 3 - Parent'),
        (CONNERS3_SELF, 'Conners 3 - Self'),
        (TSCYC, 'TSCYC'),
        (BRIEF2, 'BRIEF2'),
        (SRS2, 'SRS2'),
        (SCARED, 'SCARED'),
        (TSCC, 'TSCC'),
    )
    test_type = models.CharField(
        max_length=16,
        choices=TEST_TYPE_CHOICES,
    )

    @property
    def client_number_str(self):
        return str(self.client_number)

    class Meta:
        ordering = ('created_at',)


class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    test = models.ForeignKey(Test, related_name='items', on_delete=models.CASCADE)
    number = models.CharField(max_length=16)
    score = models.DecimalField(max_digits=1, decimal_places=0, null=True)
    group = models.CharField(max_length=64, default='', blank=True)
    description = models.CharField(max_length=128, default='', blank=True)

    class Meta:
        ordering = ('created_at',)

    @property
    def groups(self):
        return self.group.split('|')
