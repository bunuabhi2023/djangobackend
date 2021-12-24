from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    class Meta:
        model = Student
        fields = ('__all__')

