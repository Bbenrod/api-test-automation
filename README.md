# API Test Automation – JSONPlaceholder

Proyecto de automatización de pruebas para validar el comportamiento de una API REST utilizando Python y pytest.  
Las pruebas se ejecutan sobre el servicio público:

https://jsonplaceholder.typicode.com

---

## Objetivo

Automatizar la validación de los requisitos funcionales de una API REST mediante casos de prueba diseñados bajo el comportamiento esperado (estándar REST), permitiendo:

- Detectar desviaciones respecto al comportamiento esperado
- Validar estructura y contenido de respuestas JSON
- Generar métricas objetivas de calidad
- Documentar defectos encontrados

---

## Alcance

Se prueban operaciones sobre el recurso `/posts`:

- Lectura de colecciones
- Lectura individual
- Relaciones (comments)
- Creación (POST)
- Actualización (PUT / PATCH)
- Eliminación (DELETE)
- Casos negativos (IDs inexistentes, datos inválidos)

---

## Requisitos funcionales

| ID | Descripción |
|----|------------|
| RF-1 | Retornar colecciones en formato JSON |
| RF-2 | Estructura consistente de recursos |
| RF-3 | Obtener recurso por ID |
| RF-4 | Crear recursos (POST) |
| RF-5 | Actualizar recursos (PUT/PATCH) |
| RF-6 | Eliminar recursos (DELETE) |

---

## Casos de prueba

Se implementan 13 casos de prueba:

- TC-01 a TC-09 → Happy Path
- TC-10 a TC-13 → Unhappy Path (validación y errores)

---

## Estructura del proyecto

```

.
├── config/
│   ├── config.py
│   ├── endpoints.py
│   └── runtime.py
│
├── tests/
│   └── posts/
│       ├── test_tc_01_get_posts.py
│       ├── ...
│       └── test_tc_13_delete_invalid.py
│
├── evidence/
│   ├── latest/
│   │   ├── metrics.txt
│   │   └── execution.txt
│   └── history/
│
├── run_tests.py
├── requirements.txt
└── README.md

````

---

## Instalación

1. Clonar el repositorio:

```bash
git clone <repo-url>
cd api-test-automation
````

2. Crear entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución de pruebas

```bash
python run_tests.py
```

---

## Resultados generados

Después de ejecutar, se generan automáticamente:

### evidence/latest/

* metrics.txt → métricas de ejecución
* execution.txt → resultados detallados por caso

### evidence/history/

* Historial de ejecuciones con timestamp

---

## Métricas generadas

El sistema calcula automáticamente:

* Total de casos ejecutados
* Casos PASS / FAIL
* Porcentaje de éxito
* Defectos encontrados
* Cobertura de pruebas
* Requisitos afectados

---

## Ejemplo de salida

```
Total casos ejecutados: 13
Casos pasados: 9 (69%)
Casos fallidos: 4 (31%)
Defectos encontrados: 4
```

---

## Defectos identificados

| ID   | Descripción                                    |
| ---- | ---------------------------------------------- |
| D-01 | POST acepta datos inválidos                    |
| D-02 | PUT retorna 500 en recurso inexistente         |
| D-03 | PATCH permite actualizar recursos inexistentes |
| D-04 | DELETE permite eliminar recursos inexistentes  |

---

## Enfoque de pruebas

Las pruebas están diseñadas con base en:

* Comportamiento esperado de una API REST
* No en el comportamiento actual del sistema

Esto permite identificar defectos reales y desviaciones funcionales.

---

## Tecnologías utilizadas

* Python
* pytest
* requests

---

## Notas

* JSONPlaceholder es una API simulada, por lo que algunos comportamientos no siguen completamente REST
* Los resultados pueden variar dependiendo del comportamiento del servicio

---


