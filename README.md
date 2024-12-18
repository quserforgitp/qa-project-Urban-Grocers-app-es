# 🚀 **API Urban Grocers ~ Creación de un kit para el usuario o usuaria  (dentro de un usuario o usuaria particular, no una tarjeta)**  
Conjunto de pruebas automatizadas para validar la creación de kits para usuarios a través de la API. Garantiza el cumplimiento de las reglas de validación de entrada para el parámetro `name` que corresponde al nombre del kit a crear bajo el usuario especificado a traves del header `Authorization` (Bearer {token}).

---

## 📝 **Descripción**  
Este proyecto contiene pruebas automatizadas para validar el endpoint de creación de kits basada en usuarios. Se comprueban casos positivos y negativos según las reglas del negocio.

---

## 📋 **Requisitos**  

Asegúrate de tener instaladas las siguientes herramientas:

- **Python >= 3.x**
- [Librerías necesarias](#my-custom-anchor-instalacion) (`requests` y `pytest`)
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
│-- requirements.txt               # Contiene la lista de dependencias para poder ejecutar correctamente el proyecto
```

---

## 🔧 **Instalación y Configuración**  

**1. Clona el repositorio:**

> [!NOTE]  
> ✅ Usuarios de PyCharm:
Si quieres clonar este repositorio directamente desde PyCharm, te puede interesar visitar este enlace:
[Guía oficial de PyCharm para clonar repositorios de GitHub](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)

*O bien, puedes utilizar directamente la linea de comandos*
   ```bash
   git clone https://github.com/quserforgitp/qa-project-Urban-Grocers-app-es.git
   cd qa-project-Urban-Grocers-app-es
   ```
   
**2. Instala las dependencias requeridas:**
<a name="my-custom-anchor-instalacion"></a>
> [!NOTE]  
> ✅ Usuarios de PyCharm:
Si quieres instalar las dependencias desde `requirements.txt` directamente en PyCharm, te puede interesar visitar este enlace:
[Guía oficial de PyCharm para gestionar dependencias de un `requirements.txt`](https://www.jetbrains.com/help/pycharm/managing-dependencies.html#apply_dependencies)

*O bien, puedes utilizar directamente la linea de comandos*
 ```bash
 pip install -r requirements.txt
 ```
---

## 🚦 **Casos de Prueba**  

| **Prueba**                                                               | **Descripción**               | **Resultado Esperado**           |
|--------------------------------------------------------------------------|-------------------------------|---------------------------------|
| `test_1_create_kit_for_user_1_letter_in_name_get_success_response` | El nombre tiene 1 caracter. | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud         |
| `test_2_create_kit_for_user_511_letters_in_name_get_success_response` | El nombre tiene 511 caracteres. | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud         |
| `test_3_create_kit_for_user_0_letters_in_name_get_error_response` | El nombre tiene 0 caracteres. | Código de respuesta: 400 |
| `test_4_create_kit_for_user_512_letters_in_name_get_error_response` | El nombre tiene 512 caracteres. | Código de respuesta: 400 |
| `test_5_create_kit_for_user_special_characters_in_name_get_success_response` | El nombre tiene caracteres especiales. | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud         |
| `test_6_create_kit_for_user_contains_blank_characters_in_name_get_success_response` | El nombre tiene espacios. | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud         |
| `test_7_create_kit_for_user_contains_numbers_in_name_get_success_response` | El nombre tiene numeros. | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud         |
| `test_8_create_kit_for_user_without_parameter_name_get_error_response` | El campo no se pasa en la solicitud. | Código de respuesta: 400 |
| `test_9_create_kit_for_user_with_value_type_number_in_name_get_error_response` | El nombre se pasa con un tipo diferente de dato (numerico). | Código de respuesta: 400 |



---

## ▶️ **Ejecución de las Pruebas**  
> [!WARNING]
> Recuerda actualizar la URL base de la API en el archivo `configuration.py` en la variable `URL_SERVICE` para que las pruebas se ejecuten correctamente

![image](https://github.com/user-attachments/assets/4bab705c-b81f-402a-a5f9-077082fcbd80)


> [!NOTE]  
> ✅ Usuarios de PyCharm:
> Si quieres ejecutar las pruebas directamente en PyCharm, sigue estos pasos

![Ejecutar pruebas desde PyCharm](https://github.com/user-attachments/assets/88215733-faa3-4192-8ad3-21b7600a85ee)


*O si prefieres tambien las puedes ejecutar utilizando el siguiente comando:*

```bash
python -m pytest create_kit_name_kit_test
```

---

## 📚 **Explicación del Código**  

### **Funciones Principales**  
   > **`positive_assert(kit_name)`**

   - Verifica que la creación de un kit con el nombre proporcionado en `kit_name` sea exitosa. Valida que el código de estado sea 201 y que el campo `"name"` en la respuesta coincida con el nombre enviado.

   > **`negative_assert(kit_name)`**

   - Verifica que la creación de un kit con un nombre no válido o en situaciones específicas (por ejemplo, nombres vacíos o excesivamente largos) devuelva un error con el código de estado 400.

   > **`negative_assert_no_parameter(param_name)`**  
   
   - Verifica que la omisión del parámetro obligatorio `param_name` al intentar crear un kit genere un error con el código de estado 400.

### **Funciones Auxiliares**  

   > **`get_create_user_body()`**

   - Devuelve una copia del cuerpo de solicitud necesario para la creación de un usuario.

   > **`get_create_kit_body(kit_name)`**

   - Devuelve una copia del cuerpo de solicitud para la creación de un kit, actualizando el valor del campo `"name"` con el valor de `kit_name`.

   > **`get_create_kit_headers(authorization_token)`**

   - Devuelve una copia de los encabezados necesarios para la creación de un kit, incluyendo el token de autorización `authorization_token`.

   > **`extract_user_token_from_response(response)`**

   - Extrae y retorna el token de autenticación (`authToken`) de la respuesta `response`.

   > **`post_new_user_and_extract_its_token()`**

   - Crea un nuevo usuario utilizando el cuerpo generado por `get_create_user_body()` y extrae el token de autenticación del usuario creado.

---

## 🛠️ **Extensiones y Mejoras Futuras**
- Agregar más pruebas con combinaciones de caracteres.
- Implementar un archivo de configuración .env para manejar URLs y parámetros dinámicos.
- Generar reportes de pruebas con herramientas como pytest-html.

---
