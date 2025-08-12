Dashboard de Gestión de Pedidos
Descripción del Proyecto
Este proyecto es una plataforma de gestión de pedidos, con una interfaz de usuario (frontend) y una API de backend. La aplicación permite visualizar métricas clave como ingresos totales, productos vendidos y pedidos pendientes, y está diseñada para simular una arquitectura escalable en la nube utilizando servicios de AWS.

Características
Dashboard Interactivo: Muestra métricas clave en tiempo real.

Backend con Flask: Una API RESTful simple para servir los datos del dashboard.

Frontend con HTML/CSS/JS: Interfaz de usuario intuitiva y adaptable.

Simulación de AWS: Demostración de cómo se integrarían servicios como AWS Lambda y S3 para un manejo robusto de eventos.

Documentación de la API: Archivo documentation.yaml para una clara comprensión de los endpoints.

Arquitectura
El proyecto está dividido en dos componentes principales:

Frontend: Una interfaz web estática construida con HTML, CSS y JavaScript que se conecta a la API de backend para obtener y mostrar datos.

Backend: Una API RESTful desarrollada con Python y Flask que simula el procesamiento de datos y la integración con servicios en la nube.

Integración con AWS (Simulación)
Hemos simulado un flujo de eventos de pedidos utilizando dos servicios clave de AWS:

AWS Lambda: Una función sin servidor que se activaría al recibir un nuevo pedido a través del endpoint /api/orders/event. Esta función procesaría los datos del pedido.

Amazon S3: El lugar de almacenamiento de eventos. La función Lambda guardaría los detalles de cada pedido como un archivo JSON en un bucket de S3, creando un registro de eventos duradero e inmutable.

Instalación
Requisitos
Asegúrate de tener Python 3.x y pip instalados.

Pasos
Clona el repositorio:

Bash

git clone [URL_DEL_REPOSITORIO]
cd [nombre-del-proyecto]
Configura el entorno virtual e instala las dependencias del backend:

Bash

python -m venv venv
source venv/bin/activate  # En macOS/Linux
# o venv\Scripts\activate # En Windows

pip install Flask flask_cors
Ejecuta el backend:

Bash

python app.py
El servidor se iniciará en http://127.0.0.1:5000.

Abre el frontend:
Simplemente abre el archivo index.html en tu navegador web. El JavaScript en el archivo se conectará automáticamente al backend para cargar los datos.

Estructura del Proyecto
.
├── app.py              # Backend de la API (Python/Flask)
├── documentation.yaml  # Documentación de la API (OpenAPI)
├── index.html          # Frontend de la interfaz de usuario
└── style.css           # Estilos para el frontend
Endpoints de la API
La API del backend expone los siguientes endpoints:

Método	Endpoint	Descripción
GET	/api/dashboard	Obtiene las métricas y datos para el dashboard.
POST	/api/orders/event	Simula el procesamiento de un nuevo evento de pedido.
