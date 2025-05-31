# print("ASIGNACIÓN MÚLTIPLE")
# x,y,z=1,2,3
# print(x)
# print(y)
# print(z)

# x=y=z="Hola mundo"
# print(x)
# print(y)
# print(z)

# print("ASIGNACIÓN CON OPERACIONES")
# n=10
# n+=5
# print(n)
# n*=2
# print(n)

# g="Me gusta leer, "
# g+="Me gusta dormir, "
# g+="Me gusta comer."
# print(g)

# c="Me llamo "
# c+="Laly"
# c*=2
# print(c)

# print("CONCATENACIÓN")
# textox="Hello"
# textoxx="Kitty"
# resultado=textox+" "+textoxx
# print(resultado)

# día="Sábado"
# fecha=24
# result=día+" "+fecha
# print(result)

# print("BÚSQUEDA")
# mensj="Hola mañana es el día domingo de la fecha 26 de marzo del año 2025"
# buscar=mensj.find("domingo")
# print(buscar)

# print("EXTRACCIÓN")
# texto="Hola mañana es domingo del día 26 del año 2025"
# extraer=texto[0:-24]
# print(extraer)

# print("COMPARACIÓN")
# string="Hello"
# string2="Hello"
# string3="Kitty"
# print(string==string2)
# print(string2==string3)

# print("EJERCICIOS")
# print("BÚSQUEDA")
# cadena="El conocimiento es poder"
# buscar=cadena.find("conocimiento")
# buscar2=cadena.find("poder")
# print(buscar)
# print(buscar2)

# text="la práctica hace al maestro"
# result=text.find("práctica")
# resulto=text.find("maestro")
# print(result)
# print(resulto)

# texto=input("Ingrese una frase: ")
# texto1=input("Ingrese la palabra deseada: ")
# print(texto.find(texto1))

# print("EXTRACCIÓN")
# txte="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges "
# print(txte.find("Sabia"))
# print(txte.find("Caminaba"))
# print(txte.find("falanges"))
# extraer=txte[459:656]
# print(extraer)

# text="El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la humedad en el aire."
# print(text.find("Pequeños"))
# print(text.find("caliente"))
# extraer=text[446:603]
# print(extraer)

# name=input("Ingresa el nombre del estudiante: ")
# nota_1=float(input("Ingresa la primera nota: "))
# nota_2=float(input("Ingresa la segunda nota: "))
# nota_3=float(input("Ingresa la tercera nota: "))
# result=nota_1*0.2
# resul=nota_2*0.3
# resultad=nota_3*0.5
# resultado=(result+resul+resultad)//3
# print(resultado," es la nota final del estudiante ",name)