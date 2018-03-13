from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('containers/', views.ContainerListView.as_view(), name='containers'),
	path('container/<int:pk>', views.ContainerDetailView.as_view(), name='container-detail'),
	path('batches/', views.BatchListView.as_view(), name='batches'),
	path('batch/<int:pk>', views.BatchDetailView.as_view(), name='batch-detail'),
	path('recipes/', views.RecipeListView.as_view(), name='recipes'),
	path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
]