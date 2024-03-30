from rest_framework import serializers
from .models import Student, Category, Book

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = [ 'name', 'age', 'fathers_name']
        # exclude = ['id']
        fields = '__all__'

    def validate(self, data):
        if any(ch.isdigit() for ch in data['name']):
            raise serializers.ValidationError({'error': 'Name only contains letters'})

        if data['age'] <18 :
            raise serializers.ValidationError({'error': 'age must be > 18'})

        return data

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    class Meta:
        model = Book
        fields = '__all__'
        #  depth =1