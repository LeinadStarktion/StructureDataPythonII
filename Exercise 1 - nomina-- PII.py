 //Estructura de Datos 
Forma particular de organizar datos en una computadora para ser utilizados de manera eficiente, diferentes tipos de estructuras de datos se acoplan para diversos tipos de aplicaciones y algunos son altamente especializados para tareas específicas.
Son un medio para manejar enormes cantidades de datos eficientemente para usos compactos como lo son grandes bases de datos.//

//1 - Listas//

//list.append(x)://
	//Adiciona un item al final de la lista//
		//Ejemplo//
		- fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  newlist = []
for x in fruits:
  if "a" in x:
    newlist. append(x)
print(newlist)
// Imprime una lista nueva con los elementos que tengan específicamente la letra “a”//

//list.extend(iterable)://
	//Expande la lista adicionando todos los elementos del iterable//

		//Ejemplo://
		
		 NameList=["Alpha", "Wanda"]
Name2List = ["Leinad",  "Beth"]
NameList.extend(Name2List)
print (NameList)
// Agrega otra lista especificada previamente a la lista inicial 🡪 Name_List (“Alpha”, “Wanda”, “Leinad”, “Beth”)//

//list.insert(i, x)://
//Inserta un elemento en una posición especificada previamente, El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto “a.insert(0, x)” desplazando los demás hacia la derecha// ////

	//Ejemplo://

aList = [222, 'xyz', 'Klend', 'dec']

aList.insert( 3, 10100)

print ("Final List : ",aList)

“Imprimira en pantalla”:

Final List : [222, 'xyz', 	‘Klend', 101000, ‘dec']

//list.remove(x)://
//Remueve el primer elemento de la lista. En caso contrario, envia un Valuerror  de no existir el elemento llamado//
	//Ejemplo://

	Starktion= ["Leinad", "alpha", "Leirbagzero", "Aaron"]
Starktion.remove("Aaron")
// Remueve elementos específicos de una lista//



//list.pop([i])://
// Extrae elemento especificado de una lista por su posición,  Si no se específica la posición, este removerá el último elemento//
	//Ejemplo://
	aList = [200, 'xcs', 'Sarada', 'Uch'];

print ("A List : ", aList.pop());
print ("B List : ", aList.pop(2));

print (aList)

//Imprime las listas con los elementos eliminados, pero en caso de no ser especificado este remueve el último ítem en la misma; como lo es el caso de la lista A”//
//>>A List :  Uch
>>B List :  Sarada

>>A List = [002, 'xcs', 'Sarada']
>>B List = [002, 'xcs','Uch']//



//list.clear()://
// Limpia el contenido de la lista por completo//	
//Ejemplo://
Starktion= ["Leinad", "alpha", "Leirbagzero", "Aaron"]
Starktion.clear()
print (Starktion)






//list.index(x[, start[, end]])://
//Mostrará la posición en la que se encuentra el elemento en la lista especificado//
	//Ejemplo://
	aList = [555, 'ZZZ', 'Mitsuki', 'SSM'];

print ("Index for ZZZ : ", aList.index( 'ZZZ' )) ;
print ("Index for Mitsuki : ", aList.index( 'Mitsuki')) ;

//>>Index for ZZZ:  1//
//>>Index for Mitsuki:  2//

	
//list.count(x)://
//Permite hacer conteo de la cantidad de repeticiones de un elemento en una lista//
	//Ejemplo://
	aList = [777, 'bbb', 'Leirbag', 'ccc', 777];

print ("Count for 777 : ", aList.count(777));
print ("Count for Leirbag : ", aList.count('Leirbag'));

//“Los resultados de salida son los siguientes”://
//Count for 777 :  2
Count for Leirbag :  1//


list.sort(*, key=None, reverse=False):
//Imprime todos los elementos contenidos en la lista en orden alfabético y también puede ordenar una lista numérica//
	//Ejemplo://
	Starktion= ["Leinad", "alpha", "Leirbagzero", "aaron"]
	  Starktion.sort()
//list.reverse()://
// Imprime la lista principal en sentido revertido a su orden alfabético y del mismo modo a una lista numérica lo imprime por orden numérico revertido//
	//Ejemplo://
	Starktion= ["Leinad", "alpha", "Leirbagzero", "aaron"]
Starktion.sort(reverse = True)
print(Starktion)


//list.copy()://
//Imprime una lista nueva, copiando el contenido de otra previamente//
	//Ejemplo://
	Thislist = ["watermelon", "strawberry", "lemon"]
Thelist = Thislist.copy()
print(Thelist)

//>>>>Api rest<<<<<
	Postman<<//




//2 - Instrucción Del://

//Elimina secciones de una lista (especificando según su índice) o todo su contenido//


	a = [-2, 4,3.1416, 777, 969, 0.5]
del a[0]
	del a[2:4]
	del a[:]
//“Esto permite eliminar secciones de la lista, y cada posición en el transcurso del proceso se actualiza debido a la falta de los otros elementos. Finalmente una instrucción con el símbolo de doble puntuación vaciara por completo la misma”//

//3 - Tuplas //

//Son argumentos que permiten coleccionar información, la cual NO puede ser modificada con ciertos elementos que dan paso a variaciones en cómo y de qué manera se muestre la información de las listas//

	//Ejemplos Aplicados://
	thistuple = tuple (("apple", "banana", "cherry"))
print(len(thistuple))
// Imprime la cantidad de caracteres que posee una tupla//

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
//Tiene la posibilidad de imprimir tuplas con valores de booleano//



thistuple = tuple (("apple", "banana", "cherry"))
print(thistuple)
// Estipula el conjunto como una tupla y lo imprime//

thistuple = ("apple", "banana", "cherry")
print (thistuple [1])
 //Imprime el segundo elemento de la tupla//

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print (thistuple [2:5])
//Imprime los elementos de la posición dos hasta la 5 suprimiendo el p5 para mostrar//

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print (thistuple [:4])
 //Imprime los elementos desde la posición inicial hasta la p4 sin mostrar esta última//

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print (thistuple [2:])
//Imprime desde la posición dos hasta la última//

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print (thistuple [-4: -1])
//Imprime desde la p-4 hasta la p-1, teniendo en cuenta el posicionamiento de la secuencia negativa.//

x = ("apple", "banana", "cherry")
y = list(x)
y [1] = "kiwi"
x = tuple(y)
print(x)
//Imprime una lista que se reemplazo por una tupla modificada en un elemento estipulado//

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) 
print(thistuple)
//Imprime una lista con un carácter agregado para finalmente ser estipulada como una tupla 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
//Estipula el conjunto como lista, remueve “apple” y la convierte e imprime como una tupla modificada//

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red) 
//Sigue un silogismo para imprimir su posición correspondiente al primer conjunto//



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
//A partir del silogismo imprime los dos primeros valores, mas, sin embargo, a partir de la posición dos los imprime a parte como una lista cerrada “*red”//

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red) 
//Imprime el primer elemento, imprime los siguientes elementos como una lista cerrada, y finalmente reserva el último elemento como un ítem más de la tupla sin ser parte de la lista cerrada//

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
print(thistuple[i])
  	i = i + 1  
//Imprime los elementos de una tupla para pasar por todos los números de índice//

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
//Imprime la suma de dos conjuntos de tuplas//

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
//Imprime los conjuntos de una tupla multiplicado por un valor especificado, el cual serán los mismos elementos dependiendo de la cantidad a potenciar//


//4 - Sets (Conjuntos) //
//Es un conjunto de colección desordenado, inalterable y no indexado. No es posible modificar elementos, pero si eliminarlos o agregar más. Además, en el momento de ser impresos, si estos elementos dentro de un set no se encuentran ordenados, el sistema los mostrará en orden aleatorio//

thisset = {"apple", "banana", "cherry"}
print(thisset)
 //Impresión de un set//

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
//Al momento de imprimir un set este ignorara elementos que estén repetidos//
	
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
//Imprime la cantidad de caracteres contenidos en un set//

	set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
//Imprime los sets en orden//

set1 = {"abc", 34, True, 40, "male"}
print(set1)
//Imprime ordenadamente los valores desde booleano, numérico y luego en formato de string//

	myset = {"apple", "banana", "cherry"}
print(type(myset))
//Imprime la clase de método de colección utilizado//
	
thisset = {"apple", "banana", "cherry"}
for x in thisset:
 	 print(x)
//Imprime los valores del set uno por uno//

	thisset = {"apple", "banana", "cherry"}
print ("banana" in thisset) 
//Identifica si el elemento “banana” se encuentra en el set//

	thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
//Agrega el valor “Orange” al set original para ser imprimido al final con el mismo//
	thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset. update(tropical)
print(thisset) 
//Añade un set especificado a otro anteriormente estipulado en este mismo y actualizado//

	thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
//Agrega el contenido de una lista a un set//

	thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
//Remueve un elemento de un set//

	thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
//Mismo principio con la función Discard ()//

	thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
//Vacía todo el set estipulado//

	




thisset = {"apple", "banana", "cherry"}

	del thisset

	print(thisset)
//Elimina por completo el set y al ser imprimido muestra un error porque el conjunto ya no existe//

	thisset = {"apple", "banana", "cherry"}
	for x in thisset:
 		print(x)
//Recorre todo el conjunto y lo imprime//

	set1 = {"a", "b" , "c"}
	set2 = {1, 2, 3}
	set1.update(set2)
	print(set1)
//Imprime elementos de un set en otro insertados con el método update ()//
	
x = {"apple", "banana", "cherry"}
	y = {"google", "microsoft", "apple"}
	x.intersection_update(y)
	print(x)
//Imprime el valor que se encuentra en ambos sets, función similar al m.c.m//

	x = {"apple", "banana", "cherry"}
	y = {"google", "microsoft", "apple"}
	z = x.intersection(y)
	print(z)
//Regresa todos los ítems de un set a otro set con la función de intersection () en uno nuevo que muestre la intersección entre ambos//
	


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
//Imprime los elementos que no se encuentran intercedidos entre ambos conjuntos de set//
	
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
//Imprime los elementos que no se encuentran repetidos entre ambos conjuntos y los muestra en uno nuevo//

//5 - Diccionarios//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)
//Imprime el contenido del diccionario//

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964}
print(thisdict["brand"])
//Imprime un valor especifico de llave del diccionario//

thisdict = { "brand": "Ford","model": "Mustang","year": 1964, "year": 2020}
print(thisdict)
//Los valores duplicados se sobreescribiran e imprimiran//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964, "year": 2020}
print(len(thisdict))
// Imprimirá la cantidad de valores contenidos en el diccionario//

thisdict = {"brand": "Ford","electric": False,  "year": 1964,"colors": ["red", "white", "blue"}
print(thisdict)
//Imprime valores de String, numérico o booleano//

this dict = {"brand": "Ford","model": "Mustang","year": 1964}
print(type(this dict))
//Imprime el tipo de conjunto que se estableció//

thisdict ={"brand": "Ford","model": "Mustang","year": 1964}
x = thisdict["model"]
print(x)
//Delega un subconjunto a otro valor aparte para imprimirlo//

thisdict ={"brand": "Ford","model": "Mustang", "year": 1964}
x = thisdict.get("model")
print(x)
//Delega un subvalor para ser puesto en otro e imprimirlo//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
x = thisdict.keys()
print(x)
//Imprime el nombre clave de las llaves contenidas en el diccionario//




car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()
print(x)
car["color"] = "white"
print(x)
//Imprime primeramente las llaves del diccionario, luego agrega un valor al diccionario como llave e imprime el nombre clave de las llaves previamente estipuladas//


thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
x = thisdict.values()
print(x)
//Imprime los valores contenidos en cada llave del diccionario//

car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.values()
print(x) 
car["year"] = 2020
print(x)
//Imprime los valores contenidos por cada llave, luego modifica el valor de la llave “Year” a 2020 para imprimirla con esos cambio agrupados por conjuntos ajenos uno del otro con paréntesis //

car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x)
//Adiciona un nuevo ítem al diccionario, y este es impreso como un valor del conjunto principal//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
x = thisdict.items()
print(x)
//Imprime los ítems de cada llave agrupado de a pares//

car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.items()
print(x)
car["year"] = 2020
print(x)
//Imprime los ítems con el valor agregado en forma de un solo conjunto en paréntesis//
 
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
if "model" in thisdict:
print("Yes, 'model' is one of the keys in the thisdict dictionary")
//Utilizando el comando condicional de If a partir del contenido del diccionario//

thisdict ={"brand": "Ford","model": "Mustang","year": 1964}
thisdict["year"] = 2018
print(thisdict)
//Edita el ítem de la llave “year” por el valor de 2018 e imprimirlo//
thisdict = {"brand": "Ford","model": "Mustang","year": 1964
thisdict.update({"year": 2020})
print(thisdict)
//Edita y actualiza la llave “year” con el método update//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.pop("model")
print(thisdict)
//Suprime la llave de model cuando se imprime y no sale en el reporte//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.popitem()
print(thisdict)
//Remueve el último item insertado al imprimir el diccionario//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
del thisdict["model"]
print(thisdict)
//Elimina una llave entera para el resultado en la impresiòn//

thisdict ={ "brand": "Ford","model": "Mustang","year": 1964}
thisdict.clear()
print(thisdict)
//Limpia el contenido del diccionario especificado//

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
mydict = thisdict.copy()
print(mydict)
//Hace una copia del diccionario y la plasma en otro para ser impreso//

thisdict = {"brand": "Ford", "model": "Mustang","year": 1964}
mydict = dict(thisdict)
print(mydict)
//Hace una copia del diccionario original en otro con el método de dict()//
 
 
 
myfamily = {"child1" : {"name" : "Emil","year" : 2004,"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}
print(myfamily)
//Imprime un diccionario con varios de estos contenidos//
 
child1 = {
  "name" : "Emil",
  "year" : 1972}
child2 = {
  "name" : "Tobias",
  "year" : 1995}
child3 = {
  "name" : "Lemon",
  "year" : 1984}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3}
print(myfamily)
//Simplificar el proceso de impresiòn colocando los nombres de los sub diccionarios de Family//

//5.1 - Diccionarios (Iteraciones)//
thisdict ={"brand": "Ford","model": "Mustang","year": 1964}
for x in thisdict:
  print(x)
//Imprime todos los nombres de las llaves del diccionario//

thisdict ={"brand": "Ford","model": "Mustang","year": 1964}
for x in thisdict:
print(thisdict[x])
//Imprime todos los valores de las llaves del diccionario//


thisdict =( "brand": "Ford","model": "Mustang","year": 1964}
for x in thisdict.values():
print(x)
//Tambien se puede operar con el método de values//
thisdict =( "brand": "Ford","model": "Mustang","year": 1964}
for x in thisdict.keys():
  print(x)
//Imprime los nombres de las llaves//

thisdict ={"brand": "Ford","model": "Mustang","year": 1964}
for x, y in thisdict.items():
  print(x, y)
//Imprime los valores y las claves utilizando el método item()//
