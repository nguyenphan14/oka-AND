Các bước để thêm mới 1 service trong Django:
Tạo 1 project mới django-admib startproject + “tên project” \
Tạo 1 app mới trong project vừa tạo django-admin startapp + “tên app” 
Thêm các thông tin sau trong file settings.py
Thêm tên app vừa tạo trong INSTALLED_APPS 
Thêm database 
     4. Thêm đường dẫn trong file urls.py 
     5. Tạo model trong lớp model.py 
     6. Sinh các bảng trong database 
py manage.py makemigrations + “tên app” 
py manage.py migrate 




7. Thêm api trong views.py 
8. Chạy project trong 1 port mới khác với port của các project còn lại py manage runserver + “số port”


Add  models to admin:

# Register your models here.
from django.contrib import admin
from django.apps import apps


all_models = apps.get_models()


for model in all_models:
   try:
       admin.site.register(model)
   except admin.sites.AlreadyRegistered:
       pass

refs: https://codinggear.blog/how-to-register-model-in-django-admin/

