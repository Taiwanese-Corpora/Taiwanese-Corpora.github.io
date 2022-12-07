from segmented import views
from django.urls import path

urlpatterns = [
    path('query_results', views.query_results),
#   path('bigram_concordance/<str:corpus_file>/<str:w1>/<str:w2>', views.bigram_concordance)
]
