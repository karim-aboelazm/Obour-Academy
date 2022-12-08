from django.contrib import admin
from django.urls import path,include

# import setting in url file 
from django.conf import settings as st
# import statc urls in url file
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('edu.urls',namespace='edu')),
]

# adding static and media urls to urlpatterns if settings Debug is True 
if st.DEBUG:
    urlpatterns += static(st.STATIC_URL, document_root=st.STATIC_ROOT)
    urlpatterns += static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)
    
