#  App Contro de Gastos - Gestión de Finanzas Personales

**App Contro Gastos** es una aplicación de escritorio desarrollada en **Python** con **PySide6**. Permite llevar el control de ingresos y gastos, visualizando balances y generando informes visuales automáticamente.

---

### Arquitectura del Software
El proyecto sigue un patrón similar al MVC (Modelo-Vista-Controlador):

* **Modelo** (`bbdd.py`): Gestiona la persistencia de datos en una base de datos SQLite.
* **Vista** (`ui/`, `dialogo_movimiento.py`): Define la interfaz de usuario con archivos .ui compilados y clases de diálogo.
* **Controlador** (`main.py`): Orquestra la comunicación entre la base de datos y la interfaz.
* **Servicio de informes** (`generar_informes.py`): Lógica externa para procesamiento de datos con Pandas.
---

### Componentes principales
1. `ControlGastos` **(Clase Principal)**: 
   * Gestiona el QStackedWidget para cambiar entre el Tablero y los Informes.
   * Implementa la actualización de la table de movimientos
   
2. `RegistroMovimientos`:
   * Maneja la creación de la tabla movimientos, si no existe. 
   * Consultas SQL
   
3. GeneradorInformes:
   * Exporta imágenes PNG mediante la utilización de Matplotlib
   * Genera un archivo `informe.html` quese visualiza mediante una `QWebEngineView`.
---
### Tecnologías Utilizadas

* **Lenguaje:** Python 3.12+
* **GUI Framework:** PySide6 (Qt for Python)
* **Base de Datos:** SQLite3 (Persistencia local)
* **Análisis de Datos:** Pandas
* **Visualización:** Matplotlib
* **Pruebas:** Unittest
---
### Estructura del Repositorio

* `main.py`: Punto de entrada a la app.
* `bbdd/`: Módulo de gestión de base de datos.
    * `bbdd.py`: Lógica de conexión y consultas SQL.
* `ui/`: Archivos de interfaz compilados (`ventana_1.py`, `gasto.py`).
* `generar_informes.py`: Procesamiento de datos y exportación de gráficos/HTML.
* `test.py`: Pruebas unitarias para asegurar la integridad de los cálculos.

---
### Instalación y Uso

Para ejecutar el proyecto: 

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/vanesaprz/ControlGastos-Python.git
    cd ControlGastos-Python
    ```
2. Crear un entorno virtual:
    ```bash 
    # En Windows:
    python -m venv venv
    venv\Scripts\activate
    
    # En Mac/Linux:
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Instalar dependencias: 
    ```bash
    pip install -r requirements.txt
    ```
4. Ejecutar:
    ```bash
    python main.py 
    ```
---
### Posibles Implementaciones Futuras
* Metas de Ahorro: Panel para marcar objetivos financieros y seguir el proceso.
* Exportación de Datos en formato Excel o CSV
* Personalización: modo oscuro y categorías editables por el usuario


---
Desarrollado por Vanesa Pérez (2026)