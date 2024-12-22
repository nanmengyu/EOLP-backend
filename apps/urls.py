from django.http import JsonResponse
from ninja import NinjaAPI

app = NinjaAPI(title="mini-edu")

from apps.user import views as user_views

app.add_router("/user", user_views.router, tags=["用户相关"])

from apps.course import views as course_views

app.add_router("/course", course_views.router, tags=["课程相关"])
