# H2Blog / article / urls.py
# Bu url sayfasını yapmaktaki maksat daha fazla url adresinin ana dizindeki url sayfasına yığılamasını engellemek

from django.contrib import admin
from django.urls import path

# Şu anki klasördeki views'i al
from . import views 

# Bu uygulamamıza isim vermemiz önemli.
# Çünkü daha sonra 'redirect' işlemi yaptığımız zaman şu uygulamanın içindeki url'ye göre 'redirect' yap diyeceğiz
app_name = "article"

# article içindek bir tane url uygulamamızı tanımladık.
urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('comment/<int:id>',views.addComment,name = "comment"),
    
    
]