console.log("Hola mundo")
// CAMEL CASE
const alumnosCursandoEnFiuba = 100
// SNAKE CASE
const alumnos_cursando_en_fiuba = 28
// Para configs y algunas otras cosas
const ALUMNOS_CURSANDO = 12

let numero= "123"

console.log(numero)
console.log("Tipo de dato de num:",typeof numero)

numero = 123
console.log("reasigno el tipo de dato de numero")
console.log("Tipo de dato de num:",typeof numero)

const alumnos = ["pala","martin","lucas"]

for(const alumno of alumnos){
	console.log("Alumno:",alumno)
}

const alumno = {
	nombre : "pala",
	edad: 23
}

for(prop in alumno){
	console.log(prop, ":", alumno[prop])
}

const modulo = function(x,y){
    return Math.sqrt(x*x + y*y)
}

console.log(typeof modulo)
console.log(modulo(4,6))
console.log(modulo(4,6).toFixed(2))
// el primer print de la funcion es un float con todos sus decimales
// y el segundo muestra solo los dos primeros decimales
console.log(((x,y)=> x+y)(2,3)) // 2 + 3 = 5

const numeros =[1,2,3,4,5,6,7,8,9]
const filtrados = numeros.filter( x => x%2==0) 
console.log(filtrados) // la funcion anónima filtra los nrs pares