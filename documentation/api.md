# APİ Dökümantasyonu

Aktar sitesi için yazılan api database işlemleri için dökümantasyon

## Ürün ekleme

```
url = /ProductInsert
method = POST
```

*Parameters ;*
```
ürün adı : "name"
ürün içeriği : "content"
ürün fiyatı : "price"
```
*Return ;*
```
Başarılı : "True"
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```
## Kullanıcı ekleme

```
url = /UserInsert
method = POST
```

*Parameters ;*
```
Kullanıcı adı : "name"
Kullanıcı soyadı : "surname"
Kullanıcı e-posta adresi : "mail"
Kullanıcı telefon numarası : "phone_no"
Kullanıcı şifresi : "password"
```
*Return ;*
```
Başarılı : "True"
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```
## Alış veriş sepetine ekleme

```
url = /ShopCartInsert
method = POST
```

*Parameters ;*
```
Kullanıcı e-posta adresi : "user_mail"
Ürün adı : "product_name"
```
*Return ;*
```
Başarılı : "True"
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```

## Admin ekleme

```
url = /AdminInsert
method = POST
```

*Parameters ;*
```
Admin e-posta adresi : "admin_mail"
Admin şifresi : "admin_password"
```
*Return ;*
```
Başarılı : "True"
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```

## Kullanıcı sorgulama

```
url = /UserQuery
method = POST
```

*Parameters ;*
```
Kullanıcı e-posta adresi : "user_mail"
```
*Return ;*
```
Başarılı (example):
{
    "id": "d138c65588d2ab366a9729c78d00cdf9",
    "name": "Yasin",
    "surname": "Şahin",
    "phone_no": 5417252525,
    "password": "test123"
} 

Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```

## Ürün sorgulama

```
url = /ProductQuery
method = POST
```

*Parameters ;*
```
Ürün adı : "product_name"
```
*Return ;*
```
Başarılı (example):
{
    "id": "d138c65588d2ab366a9729c78d007d00",
    "name": "test 1",
    "content": "test cont",
    "price": 41.21
}

Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```
## Alış veriş sepeti sorgulama

```
url = /ShopCartQuery
method = POST
```

*Parameters ;*
```
Kullanıcı e-posta adresi : "user_mail"
```
*Return ;*
```
Başarılı (example):
{
    "1": {
        "product_id": "d138c65588d2ab366a9729c78d007d00",
        "product_name": "test 1",
        "product_content": "test cont",
        "product_price": 41.21
    },
    "2": {
        "product_id": "d138c65588d2ab366a9729c78d007d00",
        "product_name": "test 1",
        "product_content": "test cont",
        "product_price": 41.21
    }
}
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```
## Admin sorgulama

```
url = /AdminQuery
method = POST
```

*Parameters ;*
```
Admin e-posta adresi : "admin_mail"
Admin şifresi : "admin_password"
```
*Return ;*
```
Başarılı : "True"
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
```
## Alış-veriş sepetinden ürün kaldırma

```
url = /ShopCartDelete
method = POST
```

*Parameters ;*
```
Admin e-posta adresi : "user_mail"
Ürün adı : "product_name"
```
*Return ;*
```
Başarılı : "True"
Başarısız : "False"
Error : "KeyError (gönderilen parametre hatası)"
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