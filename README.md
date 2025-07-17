ProyectoCoder Este es un proyecto desarrollado con Django para la cursada de CoderHouse.

Requisitos Python 3.11 o superior pip

Instalación Clonar el repositorio git clone cd primeraApp

Crear y activar un entorno virtual (opcional pero recomendado) python -m venv .venv source .venv/bin/activate # En Windows: .venv\Scripts\activate

Instalar dependencias pip install -r requirements.txt

Configuración inicial

Aplicar migraciones python manage.py migrate

Crear un superusuario (opcional, para acceder al admin) python manage.py createsuperuser

Levantar el servidor de desarrollo python manage.py runserver El proyecto estará disponible en http://127.0.0.1:8000/app/

Estructura del proyecto core/: Aplicación principal con modelos, vistas, formularios y urls. core/templates/: Plantillas HTML.  config/: Configuración global del proyecto Django. requirements.txt: Dependencias del proyecto.  accounts/: Configuracion global de las cuentas de usuario

Comandos útiles

Aplicar migraciones: python manage.py migrate

Crear nuevas migraciones: python manage.py makemigrations

Crear superusuario: python manage.py createsuperuser

Levantar el servidor: python manage.py runserver

Notas Para agregar nuevas apps, usar: python manage.py startapp nombre_app

Para acceder al panel de administración: http://127.0.0.1:8000/admin/
