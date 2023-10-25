# import json
#
# from django.core.management import BaseCommand
#
# from main.models import Course, Lesson, Payment
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         course_list = [
#             {
#                 "name": "Python",
#                 "image": "",
#                 "description": "Python Developer"
#             },
#             {
#                 "name": "PostgreSQL",
#                 "image": "",
#                 "description": "Работа с базой данных"
#             }
#         ]
#
#         lesson_list = [
#             {
#                 "name": "Django",
#                 "image": "",
#                 "description": "Django REST Framework",
#                 "video_link": "http://sky.pro/",
#                 "course": 1
#             },
#             {
#                 "name": "Data Science",
#                 "image": "",
#                 "description": "Работа с базами данных",
#                 "video_link": "https://sky.pro/",
#                 "course": 2
#             }
#         ]
#
#         payment_list = [
#             {
#                 "user": 1,
#                 "payment_date": "2023-10-25T15:34:12.254Z",
#                 "course": 1,
#                 "payment_amount": 28500,
#                 "payment_method": "Transfer"
#             },
#             {
#                 "user": 1,
#                 "payment_date": "2023-10-25T15:58:46.531Z",
#                 "course": 2,
#                 "payment_amount": 5000,
#                 "payment_method": "Cash"
#             },
#             {
#                 "user": 1,
#                 "payment_date": "2023-10-25T15:59:21.496Z",
#                 "lesson": 1,
#                 "payment_amount": 15600,
#                 "payment_method": "Cash"
#             },
#             {
#                 "user": 1,
#                 "payment_date": "2023-10-25T15:59:46.749Z",
#                 "lesson": 2,
#                 "payment_amount": 27999,
#                 "payment_method": "Transfer"
#             }
#         ]
#         for course in course_list:
#             Course.objects.create(**course)
#
#         for lesson in lesson_list:
#             Lesson.objects.create(**lesson)
#
#         for payment in payment_list:
#             Payment.objects.create(**payment)
