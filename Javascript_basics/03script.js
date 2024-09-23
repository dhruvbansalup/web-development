// let arr=[1,6,89,6,82,3,1]
// console.log(arr)

// let a="Dhruv"
// a="Vodes"
// console.log(a.toLowerCase)
// console.log(a)

// console.log()

// let a = [1, 3, 5, 7, 9]


// for (let index = 0; index < a.length; index++) {
//     const element = a[index];
//     console.log(element)
// }

// a.forEach((value, index, arr) => {
//     console.log(value, index, arr)
// })

let obj = {
    a: 1,
    b: 2,
    c: 3
}

for (const key of obj) {
    if (Object.hasOwnProperty(obj, key)) {
        const element = obj[key];
        console.log(element)
    }
}