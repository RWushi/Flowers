import base64

category_name = ("Начало")
encoded_category_name = base64.b64encode(category_name.encode('utf-8')).decode('utf-8')
print(encoded_category_name)
