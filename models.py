from mongoengine import Document, StringField, IntField, FloatField, DateTimeField
from uuid import uuid4
from datetime import datetime

class Product(Document):
    id = StringField(primary_key=True, default= lambda: str(uuid4()))
    imageUrl = StringField(required=True)
    name = StringField(required=True, unique=True)
    category = StringField(required=True, choices=["vegetable", "snacks", "fruits"])
    stock = IntField(default=0)
    price = FloatField(required=True)
    description = StringField()

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()