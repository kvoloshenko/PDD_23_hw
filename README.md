# PDD_23_hw
Python: Django, Users. registration, authorization, rights system

## update 2022.06.06
Implemented user model: added new aplication 'usersapp'.

The menu item “Data management” (req_list.html) is available only for logged in users.

If user attribute is_dbAdmin = True than it’s possible to change data at the pages:

* req_detail.html
* req_update.html
* req_create.html
* req_delete.html

## Project
Project name is kvblog.

## Aplication:
Aplication name is 'blogapp'.

## Pages:
Implemented the base page (base.html):

![img_1.png](img_1.png)

Static is here:

![img_9.png](img_9.png)

Implemented pages inherited from the base page:

![img.png](img.png)

### index.html
index.html - the first page of the aplication;

![img_2.png](img_2.png)

### form.html
form.html - the page with the form used for search at HH.RU;

![img_3.png](img_3.png)

### result.html
result.html - the page with current result of the request at HH.RU;

![img_4.png](img_4.png)

### history.html
history.html - the page with all saved request at the db;

![img_5.png](img_5.png)

### contacts.html
contacts.html - the page with my contacts.

![img_6.png](img_6.png)

### 2022.06.06 Updated:
Added new navigation link ‘Управление данными’.

Added new pages:

* req_list.html
* req_detail.html
* req_update.html
* req_create.html
* req_delete.html

For these pages added class base views classes based on different view classes.

Added Mixin for the view classes

* Hh_RequestDetailView
* Hh_RequestUpdateView



### urls
Internal urls described here:

![img_10.png](img_10.png)

## Models:
Models names are:
* Hh_Request
* Hh_Response

![img_7.png](img_7.png)

## Django commands:
Implemented two commands:
1. fill_db - to fill database with test data;
2. fill_db_parser - to fill databsse with parsed data from HH.RU

Examples:

python manage.py fill_db

python manage.py fill_db_parser

![img_8.png](img_8.png)