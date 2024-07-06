from django.db import models
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class User(BaseModel):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    basalMetabolicRate = models.FloatField(default=0)
    userImage = models.CharField(max_length=8000, default="user_image")

    def __str__(self):
        return self.name

class Meal(BaseModel):
    name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Food(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    calories = models.FloatField(default=0)

# class ImageModel(models.Model):
#     name = models.ImageField(upload_to='media/images')