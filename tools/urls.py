from django.urls import path


from .views import (
    CategoryList,
    CategoryDetail,
    ToolsList,
    ToolsDetail,
    FeedBackList,
    FeedBackDetail,
)

urlpatterns = [
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path("category/", CategoryList.as_view(), name='category_list'),
    path('tools/<int:pk>/', ToolsDetail.as_view(), name='tools_detail'),
    path('tools/', ToolsList.as_view(), name='tools_list'),
    path('feedback/<int:pk>/', FeedBackDetail.as_view(), name='feedback_detail'),
    path('feedback/', FeedBackList.as_view(), name='feedback_list'),
]