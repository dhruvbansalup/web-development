// console.log(querySelector(".box").innerHTML);
// console.log(querySelector(".box").outerHTML);
// console.log(querySelector(".box").tagName);
// console.log(querySelector(".box").textContent);

// document.querySelector(".container").hidden = true;
document.querySelector(".box").innerHTML = "Hello";


let div=document.createElement("div");
div.innerHTML="This tag is <b>inserted</b>"
div.setAttribute("class","created")
document.querySelector(".container").append(div)

// document.querySelector(".container").before(div)



let cont=document.querySelector(".container")
cont.insertAdjacentHTML("afterend","<b>This is a new html</b> CONTENT")
cont.insertAdjacentHTML("beforebegin","<b>This is a new html</b> CONTENT")

document.querySelector(".box").remove()


