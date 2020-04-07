from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here. --> Buradaki url map'ine göre çalışacak fonksiyonlarımızı barındıran dosya.

### AŞAĞIDAKİ BÖLÜMÜN TAMAMI YENİ KULLANICI KAYDI OLUŞTURMAK İÇİN 1. YÖNTEMDİR - BU YÖNTEM DAHA KISADIR. ###
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        # form'da herhangi bir sıkıntı yoksa yani şifre-kullanıcı adı düzgünse username ve password alanını aldık;
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        # şimdi user modelinden bir obje(yeni kullanıcı) oluşturmamız gerekiyor. Daha sonra bu objeyi(yeni kullanıcı) kaydetmemiz gerekiyor. Bunu da önece en yukarıda 3.sırada ("from django.contrib.auth.models import User") ekleyerek yapaçağız.

        #kullanıcımızı oluşturmaya başlayalım;
        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save() # bu .save() işlemini de oluşturduğumuz zaman kullanıcı veritabanın kaydedilmişolacak.

        # kullanıcı kayıt olduktan sonra hemen login de olması için en yukarıda 4. sıradakini (from django.contrib.auth import login) ekleyerek yapıyoruz.
        login(request,newUser)
        messages.success(request,"Başarıyla Kayıt Oldunuz...") # kullanıcıya mesajı göstermek için;
        # artık kullanıcımız hem kayıt oldu hem de otomatik olarak giriş yapmış oldu. Bundan sonra da index sayfasına dönmesi gerekiyor bunun için (from django.shortcuts import render) importunun sonundaki, 'redirect' fonksiyonunu ekleyerek yapıyoruz.
        # 'redirect' fonksiyonunun bizi 'index' sayfasına döndürmesi için daha önce, H2Blog/urls.py'deki "path('', views.index,name = "index")," satırınada index sayfasına isim vermiştik, 'redireckt' fonksiyonunun içine bu index sayfasının adını veriyoruz. Ör: redirect("index")
        return redirect("index") # if koşulu sağlanmadı yani 'form.is_valid():' sağlanmadığı için 

    context = {
            "form" : form 
        }
    return render(request,"register.html",context)
### YUKARIDAKİ BÖLÜMÜN TAMAMI YENİ KULLANICI KAYDI OLUŞTURMAK İÇİN 1.YÖNTEMDİR ###   

#____________________________________ 2.YÖNTEM __________________________________________________________

### AŞAĞIDAKİ BÖLÜMÜN TAMAMI YENİ KULLANICI KAYDI OLUŞTURMAK İÇİN 2. YÖNTEMDİR ###
"""
def register(request):
    if request.method == "POST": # Kullanıcının yaptığı işlem POST ise kullanıcıdan aşağıda alacağıız bilgilerle form'u doldurup işlemleri yapacağız. Bu işlemler ise kullanıcı kaydı ya da işlemilerin doğru yapılmamasından kaynaklanan uyarı mesajının gösterilmesi olacak. 
        form = RegisterForm(request.POST)
        # forms.py dosyasındaki clean metodunu burda tanımlıyoruz. "clean" metodu kullanıcı bilgilerinin doğruluğunu kontrol eder.
        # form'da herhangi bir sıkıntı yoksa yani şifre ve kullanıcı adı düzgün ise aşağdaki if bloğu çalışır;
        if form.is_valid():
            # form'da herhangi bir sıkıntı yoksa yani şifre-kullanıcı adı düzgünse username ve password alanını aldık;
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # şimdi user modelinden bir obje(yeni kullanıcı) oluşturmamız gerekiyor. Daha sonra bu objeyi(yeni kullanıcı) kaydetmemiz gerekiyor. Bunu da önece en yukarıda 3.sırada ("from django.contrib.auth.models import User") ekleyerek yapaçağız.

            #kullanıcımızı oluşturmaya başlayalım;
            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save() # bu .save() işlemini de oluşturduğumuz zaman kullanıcı veritabanın kaydedilmişolacak.

            # kullanıcı kayıt olduktan sonra hemen login de olması için en yukarıda 4. sıradakini (from django.contrib.auth import login) ekleyerek yapıyoruz.
            login(request,newUser)
            # artık kullanıcımız hem kayıt oldu hem de otomatik olarak giriş yapmış oldu. Bundan sonra da index sayfasına dönmesi gerekiyor bunun için (from django.shortcuts import render) importunun sonundaki, 'redirect' fonksiyonunu ekleyerek yapıyoruz.
            # 'redirect' fonksiyonunun bizi 'index' sayfasına döndürmesi için daha önce, H2Blog/urls.py'deki "path('', views.index,name = "index")," satırınada index sayfasına isim vermiştik, 'redireckt' fonksiyonunun içine bu index sayfasının adını veriyoruz. Ör: redirect("index")
            return redirect("index") # if koşulu sağlanmadı yani 'form.is_valid():' sağlanmadığı için 
        
        context = { # if koşulu sağlanmadı yani 'form.is_valid():' sağlanmadığı için aynı sayfayı render almamız yani yeniememeiz gerekiyor, bu yüzden 'context' oluşturuyoruz.
            "form" : form 
        }
        return render(request,"register.html",context)

    else: #  kullanıcının yaptığı işlem POST değil ise sayfanın yenilenmesini sağladık.
        form = RegisterForm()
        context = {
            "form" : form 
        }
        return render(request,"register.html",context)"""
    ### YUKARIDAKİ BÖLÜMÜN TAMAMI YENİ KULLANICI KAYDI OLUŞTURMAK İÇİNDİR.###



def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password) # bu ifade; databese'e gidip böyle bir kullanıcı ve şifre var mı diye kontrol edecek, bunu eklemeden önce en yukarıda "from django.contrib.auth import login,authenticate" in sonuna 'authenticate'i ekleyerek import ediyoruz.

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,'Başarıyla Çıkış Yaptınız')
    return redirect("index")

