from django.db import models

# Create your models here.

class Quote(models.Model):
    text = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text

    class Meta:
        db_table = 'quotes'    

class Category(models.Model):
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.category

    class Meta:
        db_table = 'categories'  