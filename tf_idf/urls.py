from django.urls import path
from tf_idf.views import index, process_form

app_name = 'tf_idf'

urlpatterns = [
    path('', index, name='index'),
    path('process-form/', process_form, name='process_form'),
]
