## Running this project:


Install the project dependencies with 


```
pip install -r requirements.txt
```

run the project with command

```
python manage.py runserver
```

## URLS

Index page http://127.0.0.1:8000/products/

Product_list http://127.0.0.1:8000/products/product_list

Product_details: http://127.0.0.1:8000/products/product.id e.g. http://127.0.0.1:8000/products/2

Admin  http://127.0.0.1:8000/admin/

Register http://127.0.0.1:8000/products/register




#Search function:

Able to search both products or categories by name, products.code

if products then return results sort by product name and product price, if search key word is category, then only return category name





