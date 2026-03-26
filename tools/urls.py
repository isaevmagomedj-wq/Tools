from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, ToolsViewSet, CategoryViewSet, FeedBackViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("tools", ToolsViewSet, basename="tools")
router.register("category", CategoryViewSet, basename="category")
router.register("feedback", FeedBackViewSet, basename="feedback")

urlpatterns = router.urls
'''from .views import (
    CategoryList,
    CategoryDetail,
    ToolsList,
    ToolsDetail,
    FeedBackList,
    FeedBackDetail,
    UserDetail,
    UserList,
)'''

'''urlpatterns = [
    path("users/", UserList.as_view(), name='users_list'),
    path("users/<int:pk>/", UserDetail.as_view(), name='users_detail'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path("category/", CategoryList.as_view(), name='category_list'),
    path('tools/<int:pk>/', ToolsDetail.as_view(), name='tools_detail'),
    path('tools/', ToolsList.as_view(), name='tools_list'),
    path('feedback/<int:pk>/', FeedBackDetail.as_view(), name='feedback_detail'),
    path('feedback/', FeedBackList.as_view(), name='feedback_list'),
]
'''

