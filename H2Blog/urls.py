"""H2Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views - İşlev görünümleri
    1. Add an import:  from my_app import views --> 1. Bir içe aktarma ekleyin: my_app içe aktarma görünümlerinden
    2. Add a URL to urlpatterns:  path('', views.home, name='home') --> v  
Class-based views - Sınıf tabanlı görünümler
    1. Add an import:  from other_app.views import Home --> 1. Bir içe aktarma ekleyin: other_app.views import
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home') --> 2. urlpatterns'e bir URL ekleyin: path ('', Home.as_view (), name = 'home')
Including another URLconf - Başka bir URLconf dahil
    1. Import the include() function: from django.urls import include, path -->  1. include () işlevini içe aktarın: django.urls dizininden import include, path   
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) --> 2. urlpatterns’e bir URL ekleyin: path ('blog /', include ('blog.urls'))   
"""
   
from django.contrib import admin 
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

from article import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = "index"),
    path('about/', views.about,name = "about"),
    
    # Eğer bana 'articles' şeklinde bir kalıp gelirse sen başka bir 'url' dosyasını buraya dahil et ve sonuna o 'url' deki yazılanları da dahil et.
    # Yani 'articles'uydulamasının içindeki "article.urls" dosyasını buraya include et. Tabi bu include'u yukarıda import etmemiz de gerekiyor
    # Bunu yapmaktaki maksat daha fazla url adresinin bu sayfaya yığılamasını engellemek
    path('articles/',include("article.urls")),
    
    # user uygulamasının url bağlantısı;
    path('user/', include("user.urls")),
    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
