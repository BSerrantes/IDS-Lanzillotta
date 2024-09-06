function changesizecolor(){
    const nombre = document.getElementById("my_name")
    nombre.addEventListener("mouseover", () =>{
        nombre.style.color = "yellow"
        nombre.style.fontSize = "30px"
    })
}