class Course {
    get price() {
        return `$${this._price}`
    }

    set price(newPrice) {
        if (newPrice > 0) {
            this._price = newPrice;
        }
    }

    constructor(title, length, price) {
        this.title = title;
        this.length = length;
        this._price = price;
    }

    getLength(givenPrice) {
        return ((this.length / this._price) * givenPrice).toFixed(2);
    }

    str() {
        return `
            Course(
                title=${this.title}, 
                length=${this.length},
                price=${this.price}
            )
        `
    }
}


class PracticalCourse extends Course {
    constructor(title, length, price, numOfExercises) {
        super(title, length, price);
        this.numOfExercises = numOfExercises;
    }
}


class TheoreticalCourse extends Course {
    publish() {
        return `TheoreticalCourse publish...`
    }

}
