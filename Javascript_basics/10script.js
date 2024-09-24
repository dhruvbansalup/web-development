console.log("Hi")

let boxes=document.getElementsByClassName("box")
console.log(boxes)

boxes[2].style.backgroundColor="red"

document.getElementById("box3").style.backgroundColor="Green"

document.querySelector(".box").style.backgroundColor="yellow"

console.log(document.querySelectorAll(".box"))

document.querySelectorAll(".box").forEach(e=>{
    console.log(e)
    e.style.backgroundColor="blue"
})

e=document.getElementsByTagName("div")
console.log(e[4].matches("#box3"))