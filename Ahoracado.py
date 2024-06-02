
# crear una lista con las palabras a adivinar
lista_palabras = ['frutilla','botella','television','flores','cafetera']

# funcion (?) para elegir una palabra al azar 
# def elegir_palabra(lista_palabras) :

# crear una funcion para adivinar las letras
def palabra_en_pantalla(adivinar_letra, letras_adivinadas):
    palabra = ' ' # crear una variable a la que se le asigne una cadena vacia
    for letra in adivinar_letra: #recorrer cada letra de la palabra que esta en la lista 
        if letra in letras_adivinadas: # condicional para verificar si la letra que el usuario ingreso se encuentra dentro de la palabra
            palabra += letra  # si la letra está se agrega a la palabra en pantalla
        else:
            palabra += ' '  #si la letra no está se agrega un espacio vacio
        print(palabra)


letras_adivinadas = [] # crear una lista donde se van a guardar las letras que el usuario adivina
cantidad_intentos = 7 # inicializar una variable con la cantidad  maxima de intentos que tiene el jugador

# crear un bucle para la cantidad de intentos que tiene el jugardor para adivinar:
# mientras que la cantidad de intentos sea mayor a 0, este dentro de la cantidad permitida (7)
# y el usuario no haya adivinado la palabra se ejecuta el bucle
# Y pedir al usuario que ingrese una letra
while cantidad_intentos > 0 and cantidad_intentos < 7 :
    letras_ingresadas = (input('Ingrese la letra: '))

# funcion(?) que chequee que la letra que ingreso el usuario se encuentra dentro de la palabra a adivinar
# si es una letra es repetida informarle que ya la ingreso y que pruebre con otra
# si la letra no se encuentra dentro de la palabra pedirle al usuario que ingrese otra letra 
# y se van reduciendo la cantidad de intentos
# si la letra se encuentra dentro de la palabra que hay que adivinar agregarla a la lista de 
# letras_adivinadas

if letras_ingresadas in letras_ingresadas :
    print('ESA LETRA YA FUE INGRESADA, PROBA CON OTRA')
elif letras_ingresadas not in lista_palabras :
    cantidad_intentos -= 1
    print('PROBA CON OTRA LETRA')

# Imprimir la palabra con las letras que el usuario va adivinando (otro bucle?)

# Si el jugador acierta todas las letras imprimir un mensaje de victoria
# si el jugador gasta todos sus intentos imprimir un mensaje de derrota

if letras_ingresadas :
    print('FELICIDADES! GANASTE EL JUEGO')
else:
    print('TE QUEDASTE SIN INTENTOS! SUERTE EN LA PROXIMA')


# FIN DEL PROGRAMA






