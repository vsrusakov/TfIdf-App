from django.urls import path
from tf_idf.views import index, TfIdfListView

app_name = 'tf_idf'

urlpatterns = [
    path('', index, name='index'),
    path('process-form/', TfIdfListView.as_view(), name='process_form'),
]
