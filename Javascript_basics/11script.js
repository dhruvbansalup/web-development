console.log("Script running")
let boxes = document.getElementsByClassName("box")
// console.log(boxes)

function getRandomColor() {
    let val1 = Math.floor(Math.random() * 256);
    let val2 = Math.floor(Math.random() * 256);
    let val3 = Math.floor(Math.random() * 256);
    return `rgb(${val1},${val2},${val3})`
}

Array.from(boxes).forEach(e => {
    e.style.backgroundColor = getRandomColor()
    e.style.color=getRandomColor()
})

document.querySelector(".container").style.backgroundColor=getRandomColor()