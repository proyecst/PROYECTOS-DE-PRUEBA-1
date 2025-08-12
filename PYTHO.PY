# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Habilita CORS para permitir peticiones desde el frontend

# Datos simulados para el dashboard
dashboard_data = {
    "total_revenue": 15800.00,
    "products_sold": 25,
    "pending_orders": 65,
    "last_orders": [
        {"id": "P-001", "product": "Laptop", "quantity": 1, "status": "Entregado"},
        {"id": "P-002", "product": "Mouse", "quantity": 2, "status": "Pendiente"},
        {"id": "P-003", "product": "Teclado", "quantity": 1, "status": "Enviado"}
    ]
}

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    """
    Endpoint para obtener los datos del dashboard.
    Retorna JSON con las métricas y los últimos pedidos.
    """
    return jsonify(dashboard_data)

@app.route('/api/orders/event', methods=['POST'])
def handle_order_event():
    """
    Endpoint simulado para manejar eventos de pedidos.
    Esta función simula la integración con AWS.
    """
    # Aquí iría la lógica para procesar el evento de pedido
    # Por ejemplo, guardar el evento en S3 o activar una función Lambda
    
    # Descripción de la simulación de AWS:
    # 1. Cuando se recibe un nuevo pedido (este POST), se desencadena
    #    una **función Lambda**.
    # 2. La función Lambda procesa el pedido y almacena los detalles
    #    del evento como un archivo JSON en un bucket de **S3**.
    # 3. Este almacenamiento en S3 sirve como un registro inmutable
    #    y una fuente de datos para análisis posteriores.
    # 4. También podría notificar a otro servicio (como SQS) para
    #    procesamiento asíncrono.
    
    print("Simulando el manejo de un evento de pedido. Esto sería manejado por una función AWS Lambda que guarda el evento en S3.")
    
    # Retornamos una respuesta de éxito
    return jsonify({"message": "Evento de pedido procesado", "status": "success"}), 200

if __name__ == '__main__':
    # Para ejecutar el servidor, necesitas tener Flask instalado:
    # pip install Flask flask_cors
    app.run(debug=True)