from peewee import *
from database.database import db

class InvoiceRegistration(db.Model):
    item_category = CharField(max_length=100)
    number_invoice = CharField(unique=True)
    product_name = CharField(max_length=250)
    quantity = IntegerField()
    sector = CharField(max_length=16)
    value = DecimalField(max_digits=10, decimal_places=2)
    description = CharField(max_length=680)
    identification_document = CharField(max_length=14)
    company_name = CharField(max_length=100)
    address = CharField(max_length=180)
    date_issue= DateField()
    payment_date = DateField()
    
    
    class Meta:
        database = db
