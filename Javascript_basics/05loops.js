let a=[1,95,23,2,12,44]

// for (let index = 0; index < a.length; index++) {
//     const element = a[index];
//     console.log(element)
// }


// a.forEach((value,index,array)=>{
//     console.log(value,index,array)
// })


let Obj={
    a:131,
    b:123
}

for (const key in Obj) {
    if (Object.prototype.hasOwnProperty.call(Obj, key)) {
        const element = Obj[key];
        console.log(element)
    }
}