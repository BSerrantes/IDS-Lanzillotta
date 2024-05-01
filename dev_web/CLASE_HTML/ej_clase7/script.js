const title = document.getElementById("titulo")

title.addEventListener("mouseover", (event) => {alert("Hola")})

const changeColor = document.getElementById("change-color")

changeColor.addEventListener("click", function (event) {

    const R = randomNumber().toString()

    const G = randomNumber().toString()

    const B = randomNumber().toString()

    title.style.color = `rgb(${R},${G},${B})`

})

function randomNumber() {return (Math.random() * 256).toFixed(0)}

