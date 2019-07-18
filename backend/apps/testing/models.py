from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.utils.dateparse import parse_datetime


class Test(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tests', on_delete=models.CASCADE)
    client_number = models.DecimalField(max_digits=8, decimal_places=0)

    CBCL_6_18 = 'cbcl_6_18'
    CBCL_1_5 = 'cbcl_1_5'
    CONNERS3_PARENT = 'conners3_parent'
    CONNERS3_SELF = 'conners3_self'
    TSCYC = 'tscyc'
    BRIEF2 = 'brief2'
    BRIEFP = 'briefp'
    SRS2 = 'srs2'
    SCARED = 'scared'
    TSCC = 'tscc'
    ASRS_6_18 = 'asrs_6_18'
    ASRS_2_5 = 'asrs_2_5'
    MASC2_SELF = 'masc2_self'
    MASC2_PARENT = 'masc2_parent'
    CDI2_SELF = 'cdi2_self'
    TEST_TYPE_CHOICES = (
        (CBCL_6_18, 'CBCL 6-18'),
        (CBCL_1_5, 'CBCL 1.5-5'),
        (CONNERS3_PARENT, 'Conners 3 - Parent'),
        (CONNERS3_SELF, 'Conners 3 - Self'),
        (TSCYC, 'TSCYC'),
        (BRIEF2, 'BRIEF2'),
        (BRIEFP, 'BRIEF-P'),
        (SRS2, 'SRS2'),
        (SCARED, 'SCARED'),
        (TSCC, 'TSCC'),
        (ASRS_6_18, 'ASRS 6-18'),
        (ASRS_2_5, 'ASRS 2-5'),
        (MASC2_SELF, 'MASC 2 - Self'),
        (MASC2_PARENT, 'MASC 2 - Parent'),
        (CDI2_SELF, 'CDI 2 - Self'),
    )
    test_type = models.CharField(
        max_length=16,
        choices=TEST_TYPE_CHOICES,
    )

    archived_items = JSONField(default=list)

    @property
    def client_number_str(self):
        return str(self.client_number)

    @property
    def is_archived(self):
        return bool(self.archived_items)

    class Meta:
        ordering = ('created_at',)

    def archive_items(self):
        json_data = [
            {
                'created_at': str(item.created_at),
                'updated_at': str(item.updated_at),
                'test': str(item.test_id),
                'number': str(item.number),
                'score': str(item.score),
                'group': str(item.group),
                'description': str(item.description),
            }
            for item in self.items.all()
        ]
        self.archived_items = json_data
        self.save()
        self.items.all().delete()

    def restore_items(self):
        for json_item in self.archived_items:
            if json_item['test'] != str(self.id):
                raise ValueError(f"Item came from test {json_item['test']}, can not restore into test {self.id}")

            Item.objects.create(
                created_at=parse_datetime(json_item['created_at']),
                updated_at=parse_datetime(json_item['updated_at']),
                test=self,
                number=json_item['number'],
                score=int(json_item['score']),
                group=json_item['group'],
                description=json_item['description'],
            )
        self.archived_items = []
        self.save()


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
