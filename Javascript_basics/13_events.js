let button=document.getElementById("btn")

button.addEventListener("click", ()=>{
    document.querySelector(".box").innerHTML="Single Click"
})

button.addEventListener("dblclick", ()=>{
    document.querySelector(".box").innerHTML="Double Click"
})


button.addEventListener("mousedown", ()=>{
    document.querySelector(".box").innerHTML="Clicked"
})

button.addEventListener("mouseenter", ()=>{
    document.querySelector(".box").innerHTML="Don't Click"
})

button.addEventListener("mouseleave", ()=>{
    document.querySelector(".box").innerHTML="Good"
})
