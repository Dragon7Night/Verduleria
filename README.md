# 🥦 Verdulería San José | Sistema de Gestión de Inventario

Verdulería San José es una aplicación web desarrollada en Django 5.0 enfocada en la gestión de inventario, registro y administración de productos (frutas, verduras, etc.) y sus respectivas categorías.

## Características principales

- 🍎 **Gestión de productos y categorías:** Registro, edición, listado y eliminación (CRUD) de categorías y productos.
- 🗄️ **Persistencia de datos:** Integración nativa con **Oracle Database** mediante `oracledb`.
- 🌐 **Arquitectura Django (MVT):** Organización estructurada con soporte para interfaz dinámica utilizando DataTables y Bootstrap 5.

---

## Pre-requisitos

### Gestión de Base de Datos (Oracle)

El proyecto utiliza una base de datos **Oracle Database**.

Parámetros clave de conexión configurados:
- **Host:** `localhost`
- **Puerto:** `1522`
- **PDB / Servicio:** `FREEPDB1`
- **Usuario de prueba:** `usuario`
- **Contraseña:** `pass123`

### Python

Se recomienda utilizar Python 3.11 o superior.

Verificar versión instalada:

```bash
py --version
```

---

## Dependencias (`requirements.txt`)

El proyecto utiliza las siguientes librerías principales:

- `Django==5.0` (Framework Web)
- `oracledb==26.0.1` (Controlador nativo para Oracle Database)
- `asgiref==3.12.1`
- `cffi==2.1.1`
- `cryptography==50.0.2`
- `pycparser==3.11`
- `sqlparse==0.6.0`
- `typing_extensions==4.16.0`
- `tzdata==2026.5`

---

# Configuración de Base de Datos en Django (`settings.py`)

La conexión está configurada en `settings.py` utilizando `oracledb` con alias de compatibilidad para `cx_Oracle`:

```python
import sys
import oracledb
sys.modules['cx_Oracle'] = oracledb

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '',                       # Se define mediante el servicio en OPTIONS
        'USER': 'usuario',                 # Usuario creado en Oracle / Docker
        'PASSWORD': 'pass123',             # Contraseña del usuario
        'HOST': 'localhost',           
        'PORT': '1522',                    # Puerto mapped de la BD Oracle
        'OPTIONS': {
            'service_name': 'FREEPDB1',    # Nombre del PDB en Oracle
        },
    }
}
```

---

# Pasos para la Instalación

## 1. Ubicarse en la ruta de trabajo

```bash
cd C:/
mkdir ProyectosGit
cd ProyectosGit
```

---

## 2. Clonar el repositorio

```bash
git clone [https://github.com/Dragon7Night/Verduleria.git](https://github.com/Dragon7Night/Verduleria.git)
```

---

## 3. Acceder a la carpeta del proyecto

```bash
cd Verduleria
```

---

## 4. Crear entorno virtual (Opcional)

```bash
py -m venv .env
```

---

## 5. Activar entorno virtual (Opcional)

En Windows:
```bash
.env\Scripts\activate
```

Para desactivarlo posteriormente:
```bash
deactivate
```

---

## 6. Instalar dependencias

```bash
pip install -r requirements.txt
```

Verificar paquetes instalados:

```bash
pip list
```

---

## 7. Aplicar migraciones en Oracle

Crear las migraciones para la aplicación principal:

```bash
py manage.py makemigrations Apps.gestionApp
```

Ejecutar las migraciones para estructurar la base de datos en Oracle:

```bash
py manage.py migrate
```

---

## 8. Iniciar el servidor de desarrollo

```bash
py manage.py runserver
```

---

## Acceso a la aplicación

Una vez iniciado el servidor, abre tu navegador e ingresa a:

```text
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
```