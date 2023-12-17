# PIDS_P3
Trabajo realizado por Juan Diego González, Rafael Martínez, Sergio Melones, Jesús Rincón y Alejandro Blas Sicilia.

Pasos para la ejecución del proyecto:
1. Descarga del archivo P3_PIDS.zip y descompresión del mismo.
2. Abra una terminal de Linux/Ubuntu y acceda al directorio donde el archivo se ha descomprimido.
3. Ejecución de los siguientes comandos:
   
   `cd /P3_PIDS/P3/src` 
   `docker compose up --build -d`
   
   Es posible que al ejecutar este comando, se obtenga el siguiente Warning:
   
   ! rasa The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64/v3) and no specific platform was requested  
   En dicho caso, realizar las siguientes modificaciones:
   
   `cd /P3_PIDS/P3/src/rasa`
   
   `nano Dockerfile_actions`
   
   Sustitución de la primera línea por la siguiente "FROM rasa/rasa:3.6.15"

   `nano Dockerfile_rasa`
   
   Sustitución de la primera línea por la siguiente "FROM rasa/rasa:3.6.15"
     
   `cd ..`
   
   `docker compose down`
   
   `docker compose up --build -d`
   
4. Una vez finalizado el comando anterior, espere unos minutos hasta que se realice la correspondiente carga de los datos.
   
5. Acceda a la siguiente URL donde encontrarás nuestra aplicación desplegada: `http://localhost:5001/data`

Pd: Al acceder a la sección asociada a "Lote inicial" tenga paciencia ya que al haber muchos datos podría ir más lenta que el resto.
