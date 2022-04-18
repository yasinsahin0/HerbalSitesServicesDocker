# APİ Dökümantasyonu

Aktar sitesi için yazılan api database işlemleri için dökümantasyon

## Ürün ekleme



```
## Alış-veriş sepetindeki ürünleri satın alma

```
url = /OrdersAppend
method = POST
```

*Parameters ;*
```
Admin e-posta adresi : "user_mail"
```
*Return ;*
```
Başarılı : "True"
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```