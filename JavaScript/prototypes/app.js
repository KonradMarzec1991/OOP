class AgedPerson {
    printAge() {
        console.log(this.age);
    }
}


class Person extends AgedPerson {
    name = 'Konrad';

    constructor() {
        super();
        this.age = 30;
    }

    greet() {
        console.log('...');
    }
}

// function Person() {
//     this.age = 30;
//     this.name = 'Konrad';
//     this.greet = function () {
//         console.log('...');
//     };
// }

Person.prototype.printAge = function() {
    console.log(this.age);
}

const person = new Person();
person.greet();
person.printAge();
console.log(person.__proto__);
const p2 = new person.__proto__.constructor();
console.log(p2);
