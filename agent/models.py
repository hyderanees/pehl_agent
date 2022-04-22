from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.address

    class Meta:
        db_table = 'Site'


class Agent(models.Model):
    name = models.CharField(max_length=50, null=False, db_column='title')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, db_column='site')
    cnic = models.CharField(max_length=13, null=False, db_column='cnic')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updated_at = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'Agent'
