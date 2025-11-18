# 📚 Documentación: API REST de Productos para Tienda Web

Este proyecto implementa una **API REST de Productos (CRUD)** diseñada para servir como *backend* para una **tienda web básica**. La API permite gestionar productos con atributos esenciales como el **nombre**, la **descripción** y el **precio**.

Utiliza **Django**, **Django REST Framework (DRF)** y **MariaDB**, con una configuración especializada para garantizar la compatibilidad en entornos macOS/XAMPP.

## 🎯 Objetivo de la API

El principal objetivo es proporcionar una interfaz simple y robusta para las cuatro operaciones fundamentales de gestión de productos: **Crear**, **Leer**, **Actualizar** y **Eliminar** (CRUD).

---

## 🛠️ Configuración y Solución de Errores Críticos (macOS/XAMPP)

La configuración se enfocó en superar desafíos comunes al usar Django con MariaDB/XAMPP en macOS.

### 1. Incompatibilidad de Versión de la Base de Datos

* **Problema:** Django 5.x requería MariaDB 10.5 o posterior, mientras que el entorno utilizaba MariaDB 10.4.28.
* **Solución:** Se realizó la **degradación de Django a la versión 4.2.11 (LTS)**, que es compatible con MariaDB 10.4.x.

### 2. Conflicto de Driver Binario (PyMySQL)

* **Problema:** El *driver* nativo (`mysqlclient`) generaba el error `OperationalError: 2059` debido a conflictos de librerías binarias.
* **Solución:** Se instaló y se forzó el uso de **`PyMySQL`** (un *driver* 100% Python).

* **Código Clave para la Solución del Driver:**

    ```python
    # AuthProject/__init__.py
    import pymysql
    pymysql.install_as_MySQLdb()
    ```
    ![Configuración PyMySQL](./docs/images/01-pymysql-config.png)

* **Configuración de Conexión:** Se usa la conexión TCP/IP estándar.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'api-db',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1', # Conexión TCP/IP
            'PORT': '3306',
        }
    }
    ```
    ![Configuración de la Base de Datos](./docs/images/02-db-settings.png)

---

## 🏗️ Implementación CRUD con `viewsets.ModelViewSet`

### 1. El Por Qué de `viewsets.ModelViewSet`

Utilizamos la clase **`viewsets.ModelViewSet`** porque encapsula la lógica completa del CRUD en una única clase, lo que permite un desarrollo de API más rápido y estandarizado:
* **Abstracción de Lógica (CRUD Automático):** DRF genera automáticamente todas las funciones necesarias para `GET`, `POST`, `PUT`, `PATCH`, y `DELETE`.
* **Generación de Rutas:** Trabaja con **`DefaultRouter`** para generar automáticamente todas las rutas necesarias a partir de una sola línea de código.

### 2. Archivos Centrales de la API

* **Modelo de Datos:** Define la estructura (`name`, `description`, `price`).

    ```python
    # AuthApp/models.py
    class Products(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
    ```
    ![Modelo Products](./docs/images/03-product-model.png)

* **Vista (CRUD Automático):** Implementación minimalista del CRUD.

    ```python
    # AuthApp/views.py
    class ProductViewSet(viewsets.ModelViewSet):
        queryset = Products.objects.all()
        serializer_class = ProductSerializer
    ```
    ![Implementación del ViewSet](./docs/images/04-viewset-crud.png)

* **Rutas Generadas:** La línea que genera todos los *endpoints*.

    ```python
    # AuthApp/urls.py
    from rest_framework.routers import DefaultRouter
    from .views import ProductViewSet

    router = DefaultRouter()
    router.register('products', ProductViewSet, basename='products')

    urlpatterns = router.urls
    ```
    ![Configuración de Rutas con Router](./docs/images/05-router-urls.png)

---

## ▶️ Guía de Ejecución

1.  **Instalación de Dependencias:**
    ```bash
    pip install django==4.2.11 djangorestframework pymysql
    ```
2.  **Preparación de la Base de Datos:**
    ```bash
    python manage.py makemigrations AuthApp
    python manage.py migrate
    ```
3.  **Inicio del Servidor:**
    ```bash
    python manage.py runserver
    ```

La API estará accesible en: **`http://127.0.0.1:8000/api/products/`**

## 🧪 Endpoints de Prueba (Thunder Client)

Los siguientes *requests* confirman la funcionalidad del CRUD:

| Operación | Método | URL | Código de Estado Esperado | Demostración |
| :--- | :--- | :--- | :--- | :--- |
| **Crear** | `POST` | `/api/products/` | `201 Created` | ![POST Request](./docs/images/06-thunder-post.png) |
| **Listar** | `GET` | `/api/products/` | `200 OK` | ![GET List Request](./docs/images/07-thunder-get-list.png) |
| **Detalle** | `GET` | `/api/products/{id}/` | `200 OK` | ![GET Detail Request](./docs/images/08-thunder-get-detail.png) |
| **Actualizar** | `PATCH` | `/api/products/{id}/` | `200 OK` | ![PATCH Request](./docs/images/09-thunder-patch.png) |
| **Eliminar** | `DELETE` | `/api/products/{id}/` | `204 No Content` | ![DELETE Request](./docs/images/10-thunder-delete.png) |