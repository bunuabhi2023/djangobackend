
from django.contrib import admin
from django.urls import path
from apiproject.views import StudentViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo', student_detail),
    path('Student/', StudentViews.as_view()),
    path('Student/<int:id>', StudentViews.as_view()),

]
