from django.contrib import admin

from .models import Article,Comment

# Register your models here.(Modellerinizi buraya kaydedin.)

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    # admin sayfasında article'ların başlık, yazar ve o.tarihlerini göstermek için;
    list_display = ["title","author","created_date"]
    
    # admin sayfasında article'lardaki başlık ve o.tarihlerine tıklama linki vermek için;
    list_display_links = ["title","created_date"]
    
    # admin sayfasında article'larda arama çubuğu için;
    search_fields = ["title"]
    
    # admin sayfasında article'larda filtreleme yapmak için;
    list_filter = ["created_date"] # [içine neyi yazarsak ona göre filtreleme yapar]
    
    ## Yukarıdaki özelliklere yenilerini eklemek için (https://docs.djangoproject.com/en/2.0/ref/contrib/admin/)

    class Meta:
        model = Article