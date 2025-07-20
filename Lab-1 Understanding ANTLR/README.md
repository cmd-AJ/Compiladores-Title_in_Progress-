# 🧪 Laboratorio 1: Introducción a ANTLR

## 📋 Descripción General

En este laboratorio trabajarás con **ANTLR**, un generador de analizadores sintácticos. Hemos proporcionado un `Dockerfile` para ayudarte a configurar el entorno rápidamente. Utilizaremos Python para hacer pruebas, ya que es más sencillo que Java para pruebas pequeñas.

* **Modalidad: Individual**

## 🧰 Instrucciones de Configuración

1. **Construir y Ejecutar el Contenedor Docker**Desde el directorio raíz de este laboratorio, ejecuta el siguiente comando para construir la imagen y lanzar un contenedor interactivo:

   ```bash
   docker build --rm . -t lab1-image && docker run --rm -ti -v "$(pwd)/program":/program lab1-image
   ```
2. **Entender el Entorno**

   - El directorio `program` se monta dentro del contenedor.
   - Este contiene la **gramática de ANTLR**, un archivo `Driver.py` (punto de entrada principal) y un archivo `program_test.txt` (entrada de prueba).
3. **Generar Archivos de Lexer y Parser**Dentro del contenedor, compila la gramática ANTLR a Python con:

   ```bash
   antlr -Dlanguage=Python3 MiniLang.g4
   ```
4. **Ejecutar el Analizador**
   Usa el driver para analizar el archivo de prueba:

   ```bash
   python3 Driver.py program_test.txt
   ```

   - ✅ Si el archivo es sintácticamente correcto, **no se mostrará ningún resultado**.
   - ❌ Si existen errores, ANTLR los mostrará en la consola.
   - **Next Step:** Jueguen editando el archivo y vean los cambios en los resultados de compilación.

## 📋 Entregables

- Realice un análisis sobre la gramática de ANTLR y el archivo de Driver y comente acerca del funcionamiento de estos, es decir, explique sus partes lo más brevemente posible e indique cómo funcionan los distintos elementos de la gramática escrita en ANTLR, e.g. "Utilizar # en ANTLR sirve para...", "Un archivo .g4 tiene las siguientes secciones...", etc.
- **Video de YouTube no listado** (pero público) con sus pruebas, donde compila bien y donde no compila bien y con sus comentarios al punto anterior.
- Repo de Github con todo su código.

## 🚀 ¿Qué Sigue?

- Esta configuración es un **entorno básico** para experimentar con ANTLR.
- A medida que avances en el curso:
  - Implementarás **Visitors** o **Listeners**
  - Realizarás **análisis semántico**
- Para tus proyectos, se recomienda **extender este entorno** para soportar una arquitectura más robusta y modular.



## 📋 Entregables

- Realice un análisis sobre la gramática de ANTLR y el archivo de Driver y comente acerca del funcionamiento de estos, es decir, explique sus partes lo más brevemente posible e indique cómo funcionan los distintos elementos de la gramática escrita en ANTLR, e.g. "Utilizar # en ANTLR sirve para...", "Un archivo .g4 tiene las siguientes secciones...", etc.


Que es ANTLR (ANOTHER TOOL LANGUAGE RECOGNITION)?
Como habiamos visto en el semestre pasador, implementamos las primeras partes del compilador como realizar el lexer donde se tokeniza cada elemento para que pueda ser utilizado en el parser con la finalidad de verificar si nuestro lenguaje de prueba es correcto o no. Basicamente eso es lo que hace ANTLR pero más optimizado. 


Que aspectos podemos ver en ANTLR. 
Con tres archivos basicos observamos lo siguiente:

   Minilang.g4

Definimos en este archivo las reglas y tokens que vamos a utilizar para parsear nuestro programa de prueba y verificar si es correcto o no. En este caso se agregaron más reglas cuyas son para hacer if statements y while.

En base al archivo Minilang.g4 lo utilizaremos para generar archivos en las cuales incluyen ADF y tokens quemados para optimizar el tiempo que se ejecuta. Por otro lado tambien tenemos los modulos que dependemos para llamar el lexer y utilizarlos para el parsing. 

Una vez que tengamos el lexer y el parser preparado utilizamos el archivo de prueba para verificar si es correcto o no nuestro archivo de prueba. 

En base a esto se hace lo siguientes pasos en el Driver.py que es basicamente el main para la verificación del codigo de prueba. El driver.py utiliza las funciones como Lexer para conseguir los tokens provenientes en MiniLang.g4 que ya fueron hechos y estan en Minilang.tokens. Luego de escupir los tokens esta las agrupa para hacer el arbol sintactico para verificar que esta correcto nuestro archivo de prueba.



OJO

Observamos que algunas reglas de producción pueden ser afectadas al agregar un token de más aunque no sea significativo como por ejemplo:

   while y > 0: # "\n" se toma en cuenta lo cual nos tira error de que esparaba "{"
   {
    y = y - 1
   }


En otros casos que son comunes es que falten algunos tokens como por ejemplo
   b =  # asignaciones sin ningun valor


## Video Explicativo 
https://youtu.be/72oCWI9cRk8