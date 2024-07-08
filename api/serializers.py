from rest_framework import serializers
from . models import UserProfile, Meal, Food

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

# class ImageModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImageModel
#         fields = '__all__'

#         def get_photo_url(self, obj):
#             request = self.context.get('request')
#             photo_url = obj.fingerprint.url
#             return request.build_absolute_uri(photo_url)