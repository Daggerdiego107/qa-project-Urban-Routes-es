# Urban Routes – Automatización de Pruebas con Selenium + PyTest

Este proyecto automatiza pruebas funcionales para la plataforma web **Urban Routes**, utilizando **Selenium WebDriver**, el patrón de diseño **Page Object Model (POM)** y el framework de testing **PyTest**.

##  Tecnologías utilizadas

- Python 3.x  
- Selenium WebDriver  
- PyTest  
- Google Chrome y ChromeDriver  

##  Estructura del proyecto

- `main.py`: Contiene toda la lógica del POM y las pruebas automatizadas.  
- `data.py`: Archivo auxiliar donde defines los datos de entrada (direcciones, teléfono, tarjeta, mensajes, etc.).
- `POM` para asegurar una estructura y limpienza del codigo junto con las pruebas

##  Funcionalidades probadas

1. **Establecer Ruta y Tarifa**
   - Define dirección de origen y destino.
   - Selecciona la tarifa Comfort.

2. **Autenticación vía Teléfono**
   - Ingresa número de teléfono.
   - Captura el código de confirmación desde la red.
   - Valida el ingreso exitoso.

3. **Agregar Método de Pago**
   - Agrega una nueva tarjeta con número y código.
   - Verifica la habilitación del botón para agregar.

4. **Comentarios para el Conductor**
   - Escribe y valida un mensaje personalizado.

5. **Servicios Extra**
   - Activa el slider de "Manta y pañuelos".
   - Ordena 2 helados con botón contador.

6. **Confirmación del Pedido**
   - Finaliza el pedido.
   - Verifica que aparezca el mensaje “El conductor llegará en X min”.

##  Cómo ejecutar las pruebas

1. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
    ```
2. Asegurate de tener `ChromeDriver` instalado y compatible con tu version de Google Chrome
3. Ejecuta las pruebas con `PyTest`:
    ```bash
    pytest -s main.py
    ```
4. Datos necesarios para la ejecucion de pruebas en `data.py`

## Notas Adicionales
- Algunas pruebas requieren esperar que ciertos elementos aparezcan ya sea esperando o que una accion sea ejecutada
- El codigo para confirmar el numero telefonico en las pruebas esta comentado para que este no sea editado y rompa la funcionalidad


## Autor
Diego Antonio Navarro Ramirez