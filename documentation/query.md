# Query

## admin_login_query

```
url = /admin_login_query
method = POST

Parameters ;

admin_mail
admin_password

Return ;

Başarılı : "True"
Başarısız : "False"
Error : "Exception"
```
## user_login_query

```
url = /user_login_query
method = POST

Parameters ;

user_mail
user_password

Return ;

Başarılı : "True"
Başarısız : "False"
Error : "Exception"
```
## user_query

```
url = /user_query
method = POST

Parameters ;

user_mail

Return ;

Başarılı : 
        {'id': 1,
        'Name': 'Yasin',
        'Surname': 'Şahin',
        'Mail': 'yasin@mail.com',
        'Phone': '0541884423',
        'Password': 'test123',
        'City': 'Samsun',
        'District': 'Hançerli mahallesi',
        'Adress': 'Test adres',
        'Status': 2}

Başarısız : "False"
Error : "Exception"
```
## cart_query

```
url = /cart_query
method = POST

Parameters ;

user_id

Return ;

Başarılı : 
        {1: {   'id': 4, 
                'UserID': 1, 
                'ProductID': {'ProductID': 2, 
                                'Name': 'karabiber', 
                                'Price': 60.0, 
                                'Content': 'karabiber açıklaması', 
                                'Stok': 50, 
                                'Category': 'baharat'}, 
                'Count': 4}}

Başarısız : "False"
Error : "Exception"
```
## product_query

```
url = /product_query
method = POST

Parameters ;

product_id

Return ;

Başarılı : 
        {'ProductID': 1, 
        'Name': 'test', 
        'Price': 44.0, 
        'Content': 'test açıklama', 
        'Stok': 50, 
        'Category': 'test category'}

Başarısız : "False"
Error : "Exception"
```
## product_last_five_query

```
url = /product_last_five_query
method = POST

Parameters ;

yok

Return ;

Başarılı : 
        {1: {'ProductID': 15, 'Name': 'Tarhun', 'Price': 13.0, 'Content': 'Tarhun açıklaması', 'Stok': 147, 'Category': 'baharat'}, 
        2: {'ProductID': 14, 'Name': 'Yenibahar', 'Price': 321.0, 'Content': 'Yenibahar açıklaması', 'Stok': 55, 'Category': 'ot'}, 
        3: {'ProductID': 13, 'Name': 'Zencefil', 'Price': 130.0, 'Content': 'Zencefil açıklaması', 'Stok': 74, 'Category': 'ot'}, 
        4: {'ProductID': 12, 'Name': 'Beyaz Biber', 'Price': 56.0, 'Content': 'Beyaz Biber açıklaması', 'Stok': 110, 'Category': 'ot'}, 
        5: {'ProductID': 11, 'Name': 'Nane', 'Price': 74.0, 'Content': 'Nane açıklaması', 'Stok': 85, 'Category': 'ot'}}


Başarısız : "False"
Error : "Exception"
```
## top_sellers_query

```
url = /top_sellers_query
method = POST

Parameters ;

count

Return ;

Başarılı : 
        {1: {'ProductID': 2, 'Name': 'karabiber', 'Price': 60.0, 'Content': 'karabiber açıklaması', 'Stok': 50, 'Category': 'baharat'},
         2: {'ProductID': 3, 'Name': 'Tuz', 'Price': 5.0, 'Content': 'Tuz açıklaması', 'Stok': 20, 'Category': 'baharat'}}


Başarısız : "False"
Error : "Exception"
```
## image_query

```
url = /image_query
method = POST

Parameters ;

product_id

Return ;

Başarılı : 
        {1: {'ProductID': 1, 'URL': 'url1'}, 
        2: {'ProductID': 1, 'URL': 'url1'}, 
        3: {'ProductID': 1, 'URL': 'url2'}}


Başarısız : "False"
Error : "Exception"
```
## product_price_query
ürün adedi ile fiyatının çarpımını döner

```
url = /product_price_query
method = POST

Parameters ;

product_id
product_count

Return ;

Başarılı : 180.0
Başarısız : "False"
Error : "Exception"
```
## random_product_query

```
url = /random_product_query
method = POST

Parameters ;

count

Return ;

Başarılı : 
            {1: {'ProductID': 6, 'Name': 'Kimyon', 'Price': 70.0, 'Content': 'Kimyon açıklaması', 'Stok': 20, 'Category': 'baharat'}, 
            2: {'ProductID': 7, 'Name': 'Kekik', 'Price': 45.0, 'Content': 'Kekik açıklaması', 'Stok': 100, 'Category': 'baharat'}, 
            3: {'ProductID': 15, 'Name': 'Tarhun', 'Price': 13.0, 'Content': 'Tarhun açıklaması', 'Stok': 147, 'Category': 'baharat'}}

Başarısız : "False"
Error : "Exception"
```
## product_list_query

```
url = /product_list_query
method = POST

Parameters ;

page_number

Return ;

Başarılı : 
            {1: {'ProductID': 12, 'Name': 'Beyaz Biber', 'Price': 56.0, 'Content': 'Beyaz Biber açıklaması', 'Stok': 110, 'Category': 'ot'}, 
            2: {'ProductID': 11, 'Name': 'Nane', 'Price': 74.0, 'Content': 'Nane açıklaması', 'Stok': 85, 'Category': 'ot'}, 
            3: {'ProductID': 10, 'Name': 'Köri', 'Price': 15.0, 'Content': 'Köri açıklaması', 'Stok': 36, 'Category': 'baharat'}, 
            4: {'ProductID': 9, 'Name': 'Kakule', 'Price': 90.0, 'Content': 'Kakule açıklaması', 'Stok': 312, 'Category': 'baharat'}, 
            5: {'ProductID': 8, 'Name': 'Çörek Otu', 'Price': 20.0, 'Content': 'Çörek Otu açıklaması', 'Stok': 80, 'Category': 'ot'}, 
            6: {'ProductID': 7, 'Name': 'Kekik', 'Price': 45.0, 'Content': 'Kekik açıklaması', 'Stok': 100, 'Category': 'baharat'}, 
            7: {'ProductID': 6, 'Name': 'Kimyon', 'Price': 70.0, 'Content': 'Kimyon açıklaması', 'Stok': 20, 'Category': 'baharat'}, 
            8: {'ProductID': 5, 'Name': 'Zerdeçal', 'Price': 40.0, 'Content': 'Zerdeçal açıklaması', 'Stok': 10, 'Category': 'baharat'}, 
            9: {'ProductID': 4, 'Name': 'Biber', 'Price': 90.0, 'Content': 'Biber açıklaması', 'Stok': 70, 'Category': 'baharat'}, 
            10: {'ProductID': 3, 'Name': 'Tuz', 'Price': 5.0, 'Content': 'Tuz açıklaması', 'Stok': 20, 'Category': 'baharat'}, 
            11: {'ProductID': 2, 'Name': 'karabiber', 'Price': 60.0, 'Content': 'karabiber açıklaması', 'Stok': 50, 'Category': 'baharat'}, 
            12: {'ProductID': 1, 'Name': 'test', 'Price': 44.0, 'Content': 'test açıklama', 'Stok': 50, 'Category': 'test category'}}


Başarısız : "False"
Error : "Exception"
```
## cart_price_count_query

```
url = /cart_price_count_query
method = POST

Parameters ;

user_id

Return ;

Başarılı : 
        {
            "total_product": 6,
            "total_price": 160.0
        }
Error : "Exception"
```
## total_product_page_count

```
url = /total_product_page_count
method = POST

Parameters ;

YOK

Return ;

Başarılı : 
        {
            'product_count': 15, 
            'page_count': 2
        }
Error : "Exception"
```