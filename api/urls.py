from api.spectacular.urls import urlpatterns as doc_urls
from peoples.urls import urlpatterns as people_urls

app_name = 'api'

urlpatterns = []

urlpatterns += doc_urls
urlpatterns += people_urls
