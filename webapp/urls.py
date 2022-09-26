from django.urls import path
from webapp.views.tasks import add_view, detail_view
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view),
    path('tasks/add/', add_view),
    path('tasks/', detail_view)
]