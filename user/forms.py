from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length= 50, label= "Kullanıcı Adı")
    password = forms.CharField(max_length= 20, label= "Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length= 20, label= "Parolayı Doğrula", widget=forms.PasswordInput)

    # bu fonksiyonda kullanıcı bilgilerinin doğruluğunu kontrol edeceğiz.
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        # parola ve confirm alanı doldurulmuş mu? ve password confirme eşit mi?
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalr Eşleşmiyor!")
        # eğer yukarıdaki şartlarda sıkıntı yoksa if durumuna girmeyeceğiz, return ile yukarıdaki alanları dönmemiz gerekiyor.
        # yukarıdki alanları bir sonraki sayfaya dönmek için bunu sözlük yapısı şeklinde dönmemiz gerekiyor.
        # bunun içinde values ismiinde bir sözlük yapısı oluşturuyoruz. Bir sonraki sayfada username'i username anahtar kelimesiyele almak istiyoruz.
        
        values = {
            "username" : username,
            "password" : password
        }
        return values 
        # form kısmını bitirdik şimdi bunu register.html'de göstermem gerekiyor.

        
        ## form uygulamasıyla ilgili diğer kullanımlar için: https://docs.djangoproject.com/en/3.0/ref/forms/api/