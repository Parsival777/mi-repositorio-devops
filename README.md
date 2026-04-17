# Proyecto Integrador DevOps - Pipeline CI/CD

Este repositorio contiene la implementación práctica de la Actividad 3 de la materia Fundamentos de DevOps. El proyecto consiste en una aplicación web desarrollada en Python (Flask), contenerizada con Docker, y automatizada mediante un pipeline de Integración y Entrega Continua (CI/CD).

##  Tecnologías Utilizadas

* **Desarrollo:** Python 3.9, Flask
* **Contenerización:** Docker, Docker Compose
* **Integración Continua (CI):** GitHub Actions
* **Simulación AWS (CD):** Estructura de AWS CodeBuild y CodeDeploy

##  Estructura del Proyecto

El repositorio está organizado de la siguiente manera para separar la lógica de la aplicación de la configuración del despliegue:

```text
mi-repositorio-devops/
├── .github/workflows/
│   └── ci-cd.yml          # Flujo automatizado de GitHub Actions
├── app/
│   ├── app.py             # Código fuente de la aplicación Flask
│   ├── Dockerfile         # Instrucciones de construcción de la imagen
│   └── requirements.txt   # Dependencias de Python
├── scripts/
│   └── start.sh           # Script de simulación para despliegue
├── docker-compose.yml     # Orquestación local del contenedor
├── buildspec.yml          # Simulación de fases para AWS CodeBuild
├── appspec.yml            # Simulación de despliegue para AWS CodeDeploy
└── README.md
```
## Instrucciones de Ejecución Local
* **Clonar el repositorio con los siguientes comandos:** 
```git clone [https://github.com/tu-usuario/mi-repositorio-devops.git](https://github.com/tu-usuario/mi-repositorio-devops.git)
cd mi-repositorio-devops
```

* **Construir y levantar el contenedor en segundo plano:**
```
docker compose up -d --build
```
* **Verifica el funcionamiento accediendo desde tu navegador**
```
http://localhost:5000
```
* **Para detener los servicios**
```
docker compose down
```