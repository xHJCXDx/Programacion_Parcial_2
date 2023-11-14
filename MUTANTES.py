class MUTANTES:
    #INICIO
    def __init__(self) -> None:
        repetir:bool = True
        while repetir == True:
            #VALIDAMOS LOS DATOS QUE INGRESA EL USUARIO PARA LA LISTA
            print("________________________________________________________________________________")
            DNA = self.VerificacionCondicionesString()
            print("________________________________________________________________________________\n")
            #MOSTRAMOS LOS DNA INGRESADOS
            print("\033[0mDNA INGRESADOS:")
            for i in range(0,len(DNA[0])):
                print(f"DNA[\033[34m{i}\033[0m]: \033[95m{DNA[i]}\033[0m")
            print("________________________________________________________________________________\n")
            #MEDIANTE LA FUNCION "isMutant()" VERIFICAMOS SI ES MUTANTE
            esMutante:bool = self.isMutant(DNA)
            #MOSTRAMOS
            if esMutante == True:
                print("Es mutante? \033[32mSI\n")
            else:
                print("Es mutante? \033[31mNO\n")
            print("\033[96m________________________________________________________________________________\033[0m")
            #Verificamos si quiere colocar otra secuencia
            verf:bool = True
            while verf == True:
                print("\n\033[92m¿Quiere verificar otra secuencia?\033[0m")
                Pverificar:str = input()
                if Pverificar.upper() == "Y":
                    repetir = True
                    verf = False
                elif Pverificar.upper() == "N":
                    repetir = False
                    verf = False
                    print("\n\033[92m<PROGRAMA FINALIZADO>\033[0m\n")
                else:
                    print(f"\n\033[31mNO ES UNA RESPUESTA VALIDA: [{Pverificar}]\033[0m")
                    verf = True
        return None
    #Es mutante?: La funcion verifica si es mutante
    def isMutant(self,DNA) -> bool:
        #VARIABLES
        esMutante:bool = False
        contador:int = 0
        Registro = []
        #SECUENCIA DE LETRAS PARA BUSCAR EN LA MATRIZ:
        Palabras = ["AAAA","TTTT","GGGG","CCCC"]
        #OPERACIONES
        MATRIZ = self.CrearMatriz(DNA)
        self.MostrarValoresMatriz(MATRIZ)
        #Buscamos la cantidad de veces que se encuentran las secuencias y realizamos el conteo de coincidencias
        Registro = self.RecorrerHorizontal(MATRIZ)  #recore la matriz en busqueda de coincidencias
        contador = self.ContadorPalabrasContenidasListas(Registro,Palabras) #cuenta la cantidad de coincidencias
        Registro = self.RecorrerVertical(MATRIZ)
        contador = contador + self.ContadorPalabrasContenidasListas(Registro,Palabras)
        Registro = self.RecorrerOblicuamenteIDI(MATRIZ)
        contador = contador + self.ContadorPalabrasContenidasListas(Registro,Palabras)
        Registro = self.RecorrerOblicuamenteDII(MATRIZ)
        contador = contador + self.ContadorPalabrasContenidasListas(Registro,Palabras)
        #Imprimimos:
        print(f"\033[32m------------------------------------\n|Cantidad TOTAL de coincidencias: \033[93m{contador}\033[32m|\n------------------------------------\033[0m")
        #RETORNO
        if contador > 1:
            esMutante = True
            return esMutante
        else:
            esMutante = False
            return esMutante
    
    #MATRIZ
    #Crea la matriz a partir de listas
    def CrearMatriz(self, DNA) -> list:
        #VARIABLES
        MATRIZ = []
        #LOOPS PARA ASIGNAR LOS VALORES A LA MATRIZ
        for i in range(0,len(DNA)):
            dna:str  = DNA[i]
            MATRIZ.append(self.SepararLetras(dna))
        return MATRIZ
    #Muesta la matriz
    def MostrarValoresMatriz(self,MATRIZ) -> None:
        #RECORRE LA MATRIZ Y MUESTRA
        for i in range(0,len(MATRIZ)):
            print("\033[97m[ ",end="")
            for j in range(0,len(MATRIZ)):
                print("\033[95m",str(MATRIZ[i][j]),end="")
                if j < len(MATRIZ)-1:
                    print("\033[97m , ", end="")
            print("\033[97m]\033[0m")
        #MUESTRA PERO NO RETORNA NADA
        return None
    #Cuenta la cantidad de coincidencias de un string con otros string dentro de una lista
    def ContadorPalabrasContenidasListas(self,Registro, Palabras) -> int:
        contador:int = 0
        for j in range(0,len(Palabras)):
            for i in range(0,len(Registro)):
                if Palabras[j] in Registro[i]:
                    contador = contador + 1
        return contador
    #Recorre una matriz de manera horizontal y arma una lista con todos los string que recorrio
    def RecorrerHorizontal(self,MATRIZ) -> list:
        Registro = []
        secuencia:str = ""
        #OPERACION
        for i in range(0,len(MATRIZ)):
            for j in range(0,len(MATRIZ)):
                secuencia = secuencia + MATRIZ[i][j]
            Registro.append(secuencia)
            secuencia = ""
        return Registro
    #Recorre una matriz de manera vertical y arma una lista con todos los string que recorrio
    def RecorrerVertical(self,MATRIZ) -> list:
        Registro = []
        secuencia:str = ""
        #OPERACION
        for i in range(0,len(MATRIZ)):
            for j in range(0,len(MATRIZ)):
                secuencia = secuencia + MATRIZ[j][i]
            Registro.append(secuencia)
            secuencia = ""
        return Registro
    #Recorre una matriz de manera oblicua(De izquierda a derecha desde el extemo inferior) y arma una lista con todos los string que recorrio
    def RecorrerOblicuamenteIDI(self,MATRIZ) -> list: 
        #Recorre la matriz de IZQUIERDA a DERECHA desde el extremo INFERIOR
        cont:int = -(len(MATRIZ)+1)
        Registro = []
        secuencia:str = ""
        condicion:bool = False
        #OPERACION
        while condicion == False: 
            for i in range(0,len(MATRIZ)):
                for j in range(0,len(MATRIZ)):
                    if i + j == len(MATRIZ)+cont:
                        secuencia = secuencia + MATRIZ[i][j]
            Registro.append(secuencia)
            
            secuencia = ""
            cont = cont + 1 
            if cont == len(MATRIZ)-1:
                condicion = True
        return Registro
    #Recorre una matriz de manera oblicua(De derecha a izquierda desde el extemo inferior) y arma una lista con todos los string que recorrio
    def RecorrerOblicuamenteDII(self,MATRIZ) -> list: 
        #Recorre la matriz de DERECHA a IZQUIERDA desde el extremo INFERIOR
        cont:int = -(len(MATRIZ))
        Registro = []
        secuencia:str = ""
        condicion:bool = False
        #OPERACION
        while condicion == False: 
            for i in range(0,len(MATRIZ)):
                for j in range(0,len(MATRIZ)):
                    if j+cont == i:
                        secuencia = secuencia + MATRIZ[i][j]
            Registro.append(secuencia)
            secuencia = ""
            cont = cont + 1 
            if cont == len(MATRIZ):
                condicion = True
        return Registro
    
    #VERIFICACION DE STRING CORRECTO
    #Unifica las diferentes verificaciones del string
    def VerificacionCondicionesString(self) -> list:
        #Verficamos que sea correcto el input que ingresa el usuario:
        #VARIABLES
        tamanio:int = 6
        DNA = []
        #LOOPS
        for i in range(0,tamanio):
            verifica:bool = False
            #VERIFICACION DE STRING INGRESADO POR EL USUARIO
            while verifica == False:
                print("\033[90m________________________________________________________________________________\033[0m")
                dna:str = self.VerificacionDeLargoCadena(f"Ingrese [\033[34m{i+1}\033[0m] DNA de la persona [\033[32mLetras:A,T,C,G\033[0m] | [\033[93mTamaño:6\033[0m] : ",tamanio)
                print("\033[90m________________________________________________________________________________\033[0m")
                verifica = self.VerificacionDeLetras(dna)
            #AÑADO EL STRING A LA LISTA
            DNA.append(dna)
        return DNA
    #Verificamos el largo de la cadena
    def VerificacionDeLargoCadena(self,texto:str,tamanio:int) -> str:
        #VERIFICAMOS EL LARGO DE LA CADENA
        ingreso:str = ""
        while tamanio != len(ingreso):
            print(texto, end="")
            ingreso = input().upper()
            #ERROR:
            if tamanio != len(ingreso):
                print(f"\033[31m-------------------------------------------\n->>>El tamaño del texto debe ser de: \033[93m{tamanio}\033[31m <<<-\n-------------------------------------------\033[0m")
        return ingreso 
    #Separa el string y lo convierte en una lista de los char que componen al string
    def SepararLetras(self,texto:str) -> list:
        #DESARMAMOS EL STRING
        DNA = []
        for i in texto:
            DNA.append(i.upper())
        return DNA
    #Verificamos que las letras ingresadas sean las correspondientes
    def VerificacionDeLetras(self,texto:str) -> bool:
        #VERIFICACION DE CUMPLIMIETO DE LETRAS
        #VARIABLES
        letrasCorrectas:bool = False
        TEXTO = self.SepararLetras(texto)
        #VERIFICAMOS LETRAS
        for i in texto:
            match i:
                case "A":
                    letrasCorrectas = True
                case "T":
                    letrasCorrectas = True
                case "C":
                    letrasCorrectas = True
                case "G":
                    letrasCorrectas = True
                case _:
                    letrasCorrectas = False
                    break
        #ERROR
        if letrasCorrectas == False:
            print("\033[31m-----------------------------------------------------\n->>>Hay por lo menos una letra que no corresponde<<<-\n-----------------------------------------------------\033[0m")
        return letrasCorrectas

#ARRANQUE(Se llama a la clase)
Mutantes = MUTANTES()