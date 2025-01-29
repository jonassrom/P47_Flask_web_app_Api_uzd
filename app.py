from flask import Flask, jsonify
from pydantic import BaseModel


app = Flask(__name__)


class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int


cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "year": 2020},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2019},
    {"id": 3, "brand": "Ford", "model": "Focus", "year": 2018},
    {"id": 4, "brand": "Nissan", "model": "Maxima", "year": 2017},
    {"id": 5, "brand": "BMW", "model": "3 Series", "year": 2016},
    {"id": 6, "brand": "Mercedes-Benz", "model": "SLR", "year": 2015},
    {"id": 7, "brand": "Audi", "model": "A3", "year": 2014},
    {"id": 8, "brand": "Volkswagen", "model": "Golf", "year": 2013},
    {"id": 9, "brand": "Kia", "model": "Rio", "year": 2012},
    {"id": 10, "brand": "Jeep", "model": "Grand Cherokee", "year": 2011},
    {"id": 11, "brand": "Chevrolet", "model": "Camaro", "year": 2010},
    {"id": 12, "brand": "Subaru", "model": "Impreza", "year": 2009},
    {"id": 13, "brand": "Dodge", "model": "Charger", "year": 2008},
    {"id": 14, "brand": "Mazda", "model": "CX-5", "year": 2007},


]


@app.route('/api/cars', methods=['GET'])
def get_cars():
    car_models = [Car.model_validate(car).model_dump() for car in cars]
    return jsonify(car_models)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
