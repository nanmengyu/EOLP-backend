from django.http import JsonResponse
from ninja import NinjaAPI

app = NinjaAPI(title="电力探客-电力知识库与在线学习平台")

from apps.user import views as user_views

app.add_router("/user", user_views.router, tags=["用户相关"])

from apps.course import views as course_views

app.add_router("/course", course_views.router, tags=["课程相关"])
