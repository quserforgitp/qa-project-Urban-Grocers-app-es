# 🚀 **API Urban Grocers ~ Creación de un kit para el usuario o usuaria  (dentro de un usuario o usuaria particular, no una tarjeta)**  
Conjunto de pruebas automatizadas para validar la creación de kits para usuarios a través de la API. Garantiza el cumplimiento de las reglas de validación de entrada para el parámetro `name` que corresponde al nombre del kit a crear bajo el usuario especificado a traves del header `Authorization` (Bearer {token}).

---

## 📝 **Descripción**  
Este proyecto contiene pruebas automatizadas para validar el endpoint de creación de kits basada en usuarios. Se comprueban casos positivos y negativos según las reglas del negocio.

---

## 📋 **Requisitos**  

Asegúrate de tener instaladas las siguientes herramientas:

- **Python >= 3.x**
- Librerías necesarias (`requests` y `pytest`)
- Archivo `sender_stand_request.py` para manejar solicitudes HTTP.
- Archivo `data.py` que contiene un diccionario con la estructura base del cuerpo de la solicitud y headers para las requests.
- Archivo `configuration.py` que contiene un la URL base de la API y los paths de los endpoints que prueban los tests.

---

## ⚙️ **Estructura del Proyecto**  

```
📂 proyecto
│-- create_kit_name_kit_test.py    # Archivo principal con pruebas automatizadas
│-- sender_stand_request.py        # Módulo que envía solicitudes HTTP
│-- data.py                        # Diccionario de datos para solicitudes
│-- configuration.py               # Contiene las URL's y paths necesarios
```

---

## 🔧 **Instalación y Configuración**  

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/quserforgitp/qa-project-Urban-Grocers-app-es.git
   cd qa-project-Urban-Grocers-app-es
   ```
   
2. Instala las dependencias requeridas:

   <div style="border-left: 6px solid #28a745; padding: 10px; margin: 10px 0; border-radius: 5px;">
    <strong>✅ Nota para usuarios de PyCharm:</strong><br>
    Si quieres instalar las dependencias desde <code>requirements.txt</code> directamente en PyCharm, te puede interesar visitar este enlace:<br>
    <a href="https://www.jetbrains.com/help/pycharm/managing-dependencies.html#apply_dependencies" target="_blank">Guía oficial de PyCharm para gestionar dependencias</a>
   </div>
   
    ```bash
    pip install -r requirements.txt
    ```
---

## 🚦 **Casos de Prueba**  

| **Prueba**                                                               | **Descripción**               | **Resultado Esperado**           |
|--------------------------------------------------------------------------|-------------------------------|---------------------------------|
| `test_crear_kit_para_usuario_1_letra_en_name_get_success_response` | El nombre tiene 1 caracteres. | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud         |

---

## ▶️ **Ejecución de las Pruebas**  

Para ejecutar las pruebas, utiliza el siguiente comando:  

```bash
python -m pytest create_kit_name_kit_test
```

---

## 📚 **Explicación del Código**  

### **Funciones Principales**  

1. **`function_name(parameter)`**  
   Brief description `parameter`.
---

## 🛠️ **Extensiones y Mejoras Futuras**
- Agregar más pruebas con combinaciones de caracteres.
- Implementar un archivo de configuración .env para manejar URLs y parámetros dinámicos.
- Generar reportes de pruebas con herramientas como pytest-html.

---

## 💻 **Ejemplo de Uso**  

Aquí un ejemplo de una prueba exitosa:  

```python
def function_name():
    positive_assert("value")
```
---