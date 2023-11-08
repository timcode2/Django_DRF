from rest_framework import serializers

from main.models import Course, Lesson, Payment, Subscription
from main.validators import YoutubeValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
