# 🧪 Unit Testing en Python

Repositorio de prácticas del **Curso de Unit Testing en Python**.  
Aquí voy documentando y aplicando de forma progresiva los conceptos de **testing automatizado** usando `unittest` (y más adelante `pytest`), con ejemplos prácticos y código propio.

> 📍 Estado actual del curso: **Clase 5 – Métodos Setup y Teardown en UnitTest**



## 🎯 Objetivo del proyecto

- Aprender a **escribir pruebas unitarias correctas en Python**
- Entender la diferencia entre **pruebas unitarias, de integración y funcionales**
- Aplicar **buenas prácticas de testing**
- Ganar soltura con `unittest` antes de pasar a `pytest`
- Construir una base sólida para proyectos reales


## 🧠 Contenidos trabajados hasta ahora

Hasta la **clase 5**, se han cubierto y aplicado los siguientes temas:

- ✔️ Qué es el testing y por qué es importante
- ✔️ Tipos de pruebas: unitarias, integración y funcionales
- ✔️ Automatización de pruebas en Python
- ✔️ Estructura básica de un proyecto de testing
- ✔️ Uso de `unittest.TestCase`
- ✔️ Métodos `setUp()` para preparar el entorno de pruebas
- ✔️ Primeros tests sobre lógica de negocio (cuenta bancaria)
- ✔️ Uso correcto de `assertEqual` y `assertRaises`
- ✔️ Validación de errores y casos límite



## 🧩 Ejemplo principal

El proyecto incluye una clase **`BankAccount`** con operaciones como:

- Depósito
- Retiro
- Transferencia
- Validación de importes
- Control de fondos insuficientes

Y su correspondiente archivo de tests donde se comprueba:

- Funcionamiento correcto (happy path)
- Manejo de errores (importes inválidos, saldo insuficiente)
- Uso adecuado de excepciones


## 🛠️ Tecnologías utilizadas

- Python 3
- `unittest`
- Git + GitHub
- Entorno virtual (`venv`)


## 🚀 Próximos pasos

A medida que avance en el curso, se incorporarán:

- `tearDown()`
- Más métodos de assert
- Organización avanzada de tests
- Mocking y simulación de dependencias
- Cobertura de código con `coverage`
- Integración continua con GitHub Actions
- Introducción a `pytest`


## 📌 Nota final

Este repositorio tiene **fines educativos**.  
Forma parte de mi proceso de aprendizaje en testing y calidad de software.  
El código irá evolucionando conforme avance en el curso y consolide conceptos.

Aprender a testear bien es aprender a **pensar mejor el código** , el profesor dice que "el código se lee, más de lo que se escribe" 🧠💻
