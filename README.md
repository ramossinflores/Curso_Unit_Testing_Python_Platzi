# 🧪 Unit Testing en Python

Repositorio de prácticas del Curso de Unit Testing en Python.
Aquí documento y aplico de forma progresiva los conceptos de testing automatizado en Python, utilizando principalmente unittest y técnicas de mocking para simular dependencias externas.

> 📍 Estado actual del curso: Clase 12 – Completado (incluyendo Coverage, CI y primera aproximación a PyTest)

## 🎯 Objetivo del proyecto

- Aprender a **escribir pruebas unitarias correctas en Python**
- Entender la diferencia entre **pruebas unitarias, de integración y funcionales**
- Aplicar **buenas prácticas de testing**
- Ganar soltura con `unittest` antes de pasar a `pytest`
- Construir una base sólida antes de dar el salto a pytest

## 🧠 Contenidos trabajados hasta ahora

Fundamentos de Testing

- Qué es el testing y por qué es importante
- Tipos de pruebas: unitarias, integración y funcionales
- Automatización de pruebas en Python
- Estructura correcta de proyectos de testing

Unittest en profundidad

- Uso de unittest.TestCase
- Métodos setUp() y tearDown()
- Métodos de assert (assertEqual, assertRaises, etc.)
- Manejo de errores y casos límite
- Uso de decoradores para omitir pruebas o marcar fallos esperados
- Convenciones de nombres para pruebas
- Organización y ejecución de test suites
- Parametrización con subTest
- Uso de doctest

Mocking y pruebas avanzadas

- Simulación de APIs externas con unittest.mock
- Uso de patch para sustituir dependencias
- Simulación de errores HTTP y fallos de red
- Uso de side_effect para lanzar excepciones y simular múltiples llamadas consecutivas
- Simulación de horarios para pruebas unitarias
- Validación de entradas (IPs válidas e inválidas) antes de llamadas externas

Datos y automatización

- Generación de datos de prueba con Faker
- Cobertura de código con coverage
- Integración continua con GitHub Actions
- Introducción a pruebas con pytest

🚀 Próximos pasos

- Profundizar en pytest

- Aplicar testing en proyectos más complejos

- Integrar pruebas en entornos reales de desarrollo

- Mejorar diseño orientado a objetos para facilitar la testabilidad

## 📌 Nota final

Este repositorio tiene **fines educativos**.  
Forma parte de mi proceso de aprendizaje en testing y calidad de software.  
El código irá evolucionando conforme avance en el curso y consolide conceptos.

Aprender a testear bien es aprender a **pensar mejor el código** , el profesor dice que **"el código se lee, más de lo que se escribe"** 🧠💻