
from django.urls import path
from book0.views import index
# gu ding xie fa
urlpatterns = [
    # path(lu you , views han shu ming)
    path('index/',index)
]