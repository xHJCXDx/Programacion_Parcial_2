# Examen Parcial 2 - Mutantes
- Apellido y Nombre: CRUZ , Hiro Julian
- Legajo: 51517
- DNI:41699553
- Email: hirojulian@gmail.com

## Proyecto Mutantes
El programa permite detectar secuencias de ADN de Mutantes y identificar si hay precensia de alguno. Se tienen encuenta los siguientes aspectos:
- La secunecia de ADN contiene 6 secuencias de 6 Bases Nitrogenadas cada una con los siguientes caracteres: A, T, C y G.
- El usuario ingresa las secuencias por fila.
- Se detecta un mutante cuando hay mas de dos secuencias de Bases nitrogenadas iguales consecutivas ("AAAA","TTTT","GGGG","CCCC"), pueden encuntrarse de modo oblicuo, vertical u horizontal.

**Nota:** Se le coloco coleres al programa(Con sintaxis **"ANSI escape sequences"**) para una mejor visualización. Esta edición no es compatible con todas las consolas, para este caso se hizo uso de Visual Studio Code, el cual no presento ningun inconveniente.

## Resolución del problema
1. Se crea una clase **MUTANTES** y se la llama para dar inicio a la aplicación:
    __Creamos la clase:__
    ``` 
    class MUTANTES:
    ```
    __Invocamos a la clase al final de codigo:__
    ``` 
    Mutantes = MUTANTES()
    ```
2. Creamos una función de inicio de la aplicación, el cual contiene el cuerpo del codigo:
    __Incio:__
    ``` 
    def __init__(self) -> None:
    ```
    Tambien se crea la función:
    ``` 
    def isMutant(self,DNA) -> bool:
    ```
    La cual es la parte esencial del codigo, ya que nos determinar si es mutante.
3. Para la solicitud de la secuencia de ADN(Debe ingresar un string con las letras:A,T,C,G y de tamaño:6), al usuario se le indicas las propiedades de este:
    ``` 
    Ingrese [1] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6]:
    ```
4. Mediante la siguiente función se verifica que el string ingresado por el usuario cumpla los requisitos:

    ``` 
    def VerificacionCondicionesString(self) -> list:
    ```
    Hacemos uso de otras funciones para particionar el funcionamiento de la funcion:
    
    __Verifica el largo de la cadena:__
    ``` 
    def VerificacionDeLargoCadena(self,texto:str,tamanio:int) -> str:
    ```
    __Convierte el string en una lista de char:__
    ``` 
    def SepararLetras(self,texto:str) -> list:
    ```
    __Verifica que las letras ingresadas sean las correspondientes:__
    ``` 
    def VerificacionDeLetras(self,texto:str) -> bool:
    ```
    **Nota:** El programa esta realizado para que no diferencie entre mayúsculas y minúsculas. También cuenta con errores que indican que condición no se esta cumpliendo.
5. Construcción de una matriz:

    ```
    def CrearMatriz(self, DNA) -> list:
    ```
    Para una mejor visualización para el usuario se creo la función:
    ```
    def MostrarValoresMatriz(self,MATRIZ) -> None:
    ```
    Esto permite visualizar la matriz de la siguiente forma:
    
    [  A ,  T ,  A ,  T ,  A ,  T]

    [  G ,  A ,  G ,  A ,  G ,  A]

    [  C ,  C ,  C ,  C ,  C ,  C]

    [  T ,  A ,  T ,  A ,  C ,  G]

    [  A ,  G ,  T ,  C ,  A ,  T]

    [  A ,  C ,  C ,  A ,  T ,  G]

6. Para realizar un recorrido por la matriz y buscar secuencias de 4 bases nitrogenadas consecutivas iguales se utilizan las siguientes 4 funciones:
    __Recorrido Horizontal:__
    ``` 
    def RecorrerHorizontal(self,MATRIZ) -> list:
    ```
    __Recorrido Vertical:__
    ``` 
    def RecorrerVertical(self,MATRIZ) -> list:
    ```
    __Recorrido Oblicuo(de izquierda a derecha desde el extemo inferior):__
    ``` 
    def RecorrerOblicuamenteIDI(self,MATRIZ) -> list: 
    ```
    __Recorrido Oblicuo(de derecha a izquierda desde el extemo inferior):__
    ``` 
    def RecorrerOblicuamenteDII(self,MATRIZ) -> list:
    ```
7. Se realiza el conteo de conincidencias, para verificar si se cumplen las condiciones, haciendo uso de la función:
    ``` 
    def ContadorPalabrasContenidasListas(self,Registro, Palabras) -> int:
    ```
8. Finalmente la función "**isMutant**" determinara si la persona es mutante y el programa mostrara el resultado. Tambien se indicara si se desea ejecutar nuevamente el programa o finalizar con la busqueda.
## USO
Se puede clonar el repositorio:

```
gh repo clone xHJCXDx/Programacion_Parcial_2
```
Otra manera es acceder al siguiente [enlace](https://github.com/xHJCXDx/Programacion_Parcial_2.git) y descargarlo.

## Casos de Prueba
### Caso 1

________________________________________________________________________________
________________________________________________________________________________
Ingrese [1] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : atatat
________________________________________________________________________________
________________________________________________________________________________
Ingrese [2] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : gagaga
________________________________________________________________________________
________________________________________________________________________________
Ingrese [3] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : cccccc
________________________________________________________________________________
________________________________________________________________________________
Ingrese [4] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : tatacg
________________________________________________________________________________
________________________________________________________________________________
Ingrese [5] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : agtcat
________________________________________________________________________________
________________________________________________________________________________
Ingrese [6] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : accatg
________________________________________________________________________________
________________________________________________________________________________

DNA INGRESADOS:
DNA[0]: ATATAT

DNA[1]: GAGAGA

DNA[2]: CCCCCC

DNA[3]: TATACG

DNA[4]: AGTCAT

DNA[5]: ACCATG
________________________________________________________________________________

[  A ,  T ,  A ,  T ,  A ,  T]

[  G ,  A ,  G ,  A ,  G ,  A]

[  C ,  C ,  **C** ,  **C** ,  **C** ,  **C**]

[  T ,  A ,  T ,  A ,  **C** ,  G]

[  A ,  G ,  T ,  **C** ,  A ,  T]

[  A ,  C ,  **C** ,  A ,  T ,  G]

------------------------------------
|Cantidad TOTAL de coincidencias: 2|
------------------------------------
Es mutante? SI

________________________________________________________________________________

¿Quiere verificar otra secuencia?

n

PROGRAMA FINALIZADO

### Caso 2

________________________________________________________________________________
________________________________________________________________________________
Ingrese [1] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : atgatc
________________________________________________________________________________
________________________________________________________________________________
Ingrese [2] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : atcgat
________________________________________________________________________________
________________________________________________________________________________
Ingrese [3] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : cgatca
________________________________________________________________________________
________________________________________________________________________________
Ingrese [4] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : atcgac
________________________________________________________________________________
________________________________________________________________________________
Ingrese [5] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : actacg
________________________________________________________________________________
________________________________________________________________________________
Ingrese [6] DNA de la persona [Letras:A,T,C,G] | [Tamaño:6] : actagc
________________________________________________________________________________
________________________________________________________________________________

DNA INGRESADOS:

DNA[0]: ATGATC

DNA[1]: ATCGAT

DNA[2]: CGATCA

DNA[3]: ATCGAC

DNA[4]: ACTACG

DNA[5]: ACTAGC
________________________________________________________________________________

[  A ,  T ,  G ,  A ,  T ,  C]

[  A ,  T ,  C ,  G ,  A ,  T]

[  C ,  G ,  A ,  T ,  C ,  A]

[  A ,  T ,  C ,  G ,  A ,  C]

[  A ,  C ,  T ,  A ,  C ,  G]

[  A ,  C ,  T ,  A ,  G ,  C]

------------------------------------
|Cantidad TOTAL de coincidencias: 0|
------------------------------------
Es mutante? NO

________________________________________________________________________________

¿Quiere verificar otra secuencia?

n

PROGRAMA FINALIZADO
