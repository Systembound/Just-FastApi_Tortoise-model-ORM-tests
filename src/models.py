from tortoise import models, fields


class PersonModel(models.Model):
    first_name: str = fields.CharField(1000)
    last_name: str = fields.CharField(1000)
