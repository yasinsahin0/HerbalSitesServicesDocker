# İNSERT

## status_insert

```
url = /status_insert
method = POST


Parameters ;

name
status_id

Return ;

Başarılı : "True"
Error : "Exception"
```
## user_insert

```
url = /user_insert
method = POST


Parameters ;

user_name
user_surname
user_mail
user_phone
user_pass
user_city
user_district
user_adress
user_status

Return ;

Başarılı : "True"
Error : "Exception"
```
## product_insert

```
url = /product_insert
method = POST


Parameters ;

product_name
product_price
product_content
product_stock
product_category

Return ;

Başarılı : "True"
Error : "Exception"
```
## product_image_insert

```
url = /product_image_insert
method = POST


Parameters ;

product_id
product_image_url

Return ;

Başarılı : "True"
Error : "Exception"
```
## cart_insert

```
url = /cart_insert
method = POST


*Parameters ;*

user_id
product_id
count

Return ;

Başarılı : "True"
Error : "Exception"
```
## order_insert

```
url = /order_insert
method = POST

Parameters ;

user_id
status

*Return ;*

Başarılı : "True"
Error : "Exception"
```
## order_detail_insert

```
url = /order_detail_insert
method = POST

Parameters ;

product_id
product_count
order_id

Return ;

Başarılı : "True"
Error : "Exception"
```