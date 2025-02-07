// const obj = {
//     name: 'Rohit',
//     arrowFunction: null,
//     normalFunction: function () {
//         this.arrowFunction = () => {
//             console.log(this.name)
//         }
//     },
// }
// obj.normalFunction()
// obj.arrowFunction()

// setTimeout(()=>console.log('hello from settimeout 1'),0)
// console.log('hello for main 1')
// setTimeout(()=>console.log('hello frm 2nd Settimeout'),0)
// console.log('main 2')

// let startNamePrinter=(name)=>{
//     let x=name.split('').reverse()
//     let handler=setInterval(()=>{
//         let y=x.pop()
//         console.log(y)
//     },1000)
//     setTimeout(()=>{
//         clearInterval(handler)

//     },(name.length+1)*1000)
// }

// startNamePrinter('orange')

// let a = [75, 55, 22, 5]; 
// console.log(a.sort());




// a={
//     name:'Abhi',
//     age:22
// };
// b=[];
// for(let i=0;i<3;i++){
//     b.push({...a})
// }
// console.log(b)
// b[1].name='Akshyay';
// console.log(b)
// console.log(b[0].name)



// x=[1,2,3,4,5,6]
// y=[...x,7,8,9]
// z=y.filter((x)=>x%2==0)
// .map((i)=>i*i)
// .reduce((a,i)=>a+i,(a=0))
// console.log(z)


// const obj = {
//     x: 1,
//     y: 1,
//     set nums(xCommay) {
//         numbers = xCommay.split(',')
//         this.x = numbers[0]
//         this.y = numbers[1]
//     },
//     get nums() {
//         return this.x + ',' + this.y
//     },
//     xPowery: function () {
//         let result = 1
//         for (let i = 1; i <= this.y; i++) {
//             result = result * this.x
//         }
//         return result
//     },
// }
// obj.nums = '2,3'
// console.log(obj.xPowery())


// const ePowerx = {
//     x: 1,
//     n: 1,
//     set parameters(param) {
//         param = param.split(' ')
//         this.x = param[0]
//         this.n = param[1]
//     },
//     get uptoNterms() {
//         let result = 1
//         let y = 1
//         for (let i = 1; i < this.n; i++) {
//             y = y * this.x
//             result = result + y
//         }
//         return result
//     },
// }
// ePowerx.parameters = '2 3'
// console.log(ePowerx.uptoNterms)


// const course = {
//     courseName: 'Modern App Dev 2',
//     courseCode: 'mad2',
// }
// const student = {
//     __proto__: course,
//     studentName: 'Rakesh',
//     studentCity: 'Delhi',
// }
// const { courseName } = student
// console.log(courseName)




api={A:'App',P:'Prog',I:'Interface'}
const standsFor=(x)=>{
    for(const [k,v] of Object.entries(api)){
        if(k!=x){
            return v
        }
    }
}

console.log(standsFor('A'))