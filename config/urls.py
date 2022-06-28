from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

#router.register(r'wo', wo_views.WorkOrderViewSet, basename="wo")

urlpatterns = [
    url(r'^', include(router.urls)),
]
