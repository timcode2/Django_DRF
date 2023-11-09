from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.models import Course, Lesson, Subscription
from main.serializers import LessonSerializer
from users.models import User

from unittest import TestCase
TestCase.maxDiff = None

class LessonCreateTestCase(APITestCase):
    """Тест кейс на создание нового урока"""
    def setUp(self) -> None:

        self.client = APIClient()

        self.user = User.objects.create(
            email='ivan@ivanov.com',
            first_name='Ivan',
            last_name='Ivanov',
            phone='88005553535',
            city='Moscow',
            role='user'
        )
        self.user.set_password('Ivanov123')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Course test',
            description='Course description'
        )

    def test_create_lesson(self):

        data = {
            'name': 'Test lesson',
            'description': 'Test description',
            'video_link': 'https://www.youtube.com/test',
            'course': self.course.id
        }

        responce = self.client.post(
            reverse('main:lesson_create'),
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            responce.json(),
            {
                "id": 1,
                "name": "Test lesson",
                "image": None,
                "description": "Test description",
                "video_link": "https://www.youtube.com/test",
                "course": 1,
                "owner": self.course.owner
            }
        )


class LessonReadTestCase(APITestCase):
    """Тест кейс на чтение записи об уроках"""
    def setUp(self) -> None:

        self.client = APIClient()

        self.user = User.objects.create(
            email='ivan@ivanov.com',
            first_name='Ivan',
            last_name='Ivanov',
            phone='88005553535',
            city='Moscow',
            role='user'
        )
        self.user.set_password('Ivanov123')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Course test',
            description='Course description'
        )

        self.lesson_1 = Lesson.objects.create(
            name='Test lesson 1 read',
            description='Test description 1 read',
            video_link='https://www.youtube.com/test_1_read',
            course=self.course,
            owner=self.user
        )

        self.lesson_2 = Lesson.objects.create(
            name='Test lesson 2 read',
            description='Test description 2 read',
            video_link='https://www.youtube.com/test_2_read',
            course=self.course
        )

    def test_read_lesson_list(self):
        """Тест на чтение списка уроков"""
        responce = self.client.get(
            reverse('main:lesson_list'),
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            responce.json(),
            {
                "count": 2,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 3,
                        "name": "Test lesson 1 read",
                        "image": None,
                        "description": "Test description 1 read",
                        "video_link": "https://www.youtube.com/test_1_read",
                        "course": 3,
                        "owner": 3
                    },
                    {
                        "id": 4,
                        "name": "Test lesson 2 read",
                        "image": None,
                        "description": "Test description 2 read",
                        "video_link": "https://www.youtube.com/test_2_read",
                        "course": 3,
                        "owner": None
                    }
                ]
            }
        )

    def test_read_single_lesson(self):
        """Тест на чтение одного урока"""
        responce = self.client.get(
            reverse('main:lesson_get', args=[self.lesson_1.id]),
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            responce.json(),
            {
                "id": 5,
                "name": "Test lesson 1 read",
                "image": None,
                "description": "Test description 1 read",
                "video_link": "https://www.youtube.com/test_1_read",
                "course": 4,
                "owner": 4
            }
        )


class LessonUpdateTestCase(APITestCase):
    """Тест кейс на изменение записи об уроках"""
    def setUp(self) -> None:

        self.client = APIClient()

        self.user = User.objects.create(
            email='ivan@ivanov.com',
            first_name='Ivan',
            last_name='Ivanov',
            phone='88005553535',
            city='Moscow',
            role='user'
        )
        self.user.set_password('Ivanov123')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Course test',
            description='Course description'
        )

        self.lesson = Lesson.objects.create(
            name='Test lesson update',
            description='Test description update',
            video_link='https://www.youtube.com/test_update',
            course=self.course,
            owner=self.user
        )

        self.data = LessonSerializer(self.lesson).data
        self.data.update({
            'name': 'Test lesson UPDATE',
            'description': 'Test description UPDATE',
            'video_link': 'https://www.youtube.com/test_UPDATE',
            'course': self.course.id,
            'owner': self.user.id,
            'image': ''
        })

    def test_put_lesson(self):
        """Тест для полного изменения урока"""

        response = self.client.put(
            reverse('main:lesson_update', args=[self.lesson.id]),
            self.data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class LessonDeleteTestCase(APITestCase):
    """Тест кейс на удаление записи об уроках"""
    def setUp(self) -> None:

        self.client = APIClient()

        self.user = User.objects.create(
            email='ivan@ivanov.com',
            first_name='Ivan',
            last_name='Ivanov',
            phone='88005553535',
            city='Moscow',
            role='user'
        )
        self.user.set_password('Ivanov123')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Course test',
            description='Course description'
        )

        self.lesson = Lesson.objects.create(
            name='Test lesson delete',
            description='Test description delete',
            video_link='https://www.youtube.com/test_delete',
            course=self.course,
            owner=self.user
        )

    def test_delete_lesson(self):

        response = self.client.delete(
            reverse('main:lesson_delete', args=[self.lesson.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionCreateTestCase(APITestCase):
    def setUp(self) -> None:

        self.client = APIClient()

        self.user = User.objects.create(
            email='ivan@ivanov.com',
            first_name='Ivan',
            last_name='Ivanov',
            phone='88005553535',
            city='Moscow',
            role='user'
        )
        self.user.set_password('Ivanov123')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Course test',
            description='Course description'
        )

    def test_create_subscription(self):

        data = {
            'course': self.course.id,
            'is_active': True
        }

        responce = self.client.post(
            reverse('main:get-subscription'),
            data=data
        )

        self.assertEqual(
            responce.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            responce.json(),
            {
                "id": 1,
                "user": 6,
                "course": 6,
                "is_active": True
            }
        )


class SubscriptionDeleteTestCase(APITestCase):
    def setUp(self) -> None:

        self.client = APIClient()

        self.user = User.objects.create(
            email='ivan@ivanov.com',
            first_name='Ivan',
            last_name='Ivanov',
            phone='88005553535',
            city='Moscow',
            role='user'
        )
        self.user.set_password('Ivanov123')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='Course test',
            description='Course description'
        )

        self.subscription = Subscription.objects.create(
            course=self.course,
            user=self.user
        )

    def test_delete_subscription(self):

        response = self.client.delete(
            reverse('main:delete-subscription', args=[self.subscription.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )