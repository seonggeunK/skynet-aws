from django.db import models

# Create your models here.
class Shop(models.Model):
    no = models.AutoField(db_column='no', primary_key=True)
    category = models.CharField(db_column='category', max_length=255)
    title = models.CharField(db_column='title', max_length=255)
    summary = models.TextField(db_column='summary', )
    subject = models.CharField(db_column='subject', max_length=255)
    contents = models.TextField(db_column='contents', )
    org_file_name = models.CharField(db_column='org_file_name', max_length=500)
    file_name = models.CharField(db_column='file_name', max_length=500)
    file_location = models.CharField(db_column='file_location', max_length=500)
    createdate = models.DateTimeField(db_column='createdate', auto_now_add=True)
    updatedate = models.DateTimeField(db_column='updatedate', auto_now=True)

    class Meta:
        managed = True
        db_table = 'shop'

    def __str__(self):
        return "Title : " + self.title + ", Summary : " + self.summary