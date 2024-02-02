from typing import Any


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int | float,
                 clean_power: int | float,
                 average_rating: int | float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> Any:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * (self.average_rating / self.distance_from_city_center))
        return round(price, 1)

    def wash_single_car(self, car: Car) -> Any:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> Any:
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income_before_wash = self.calculate_washing_price(car)
                self.wash_single_car(car)
                income += income_before_wash

        return round(income, 1)

    def rate_service(self, new_rating: int) -> Any:
        sum_of_ratings = (self.average_rating
                          * self.count_of_ratings) + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_ratings / self.count_of_ratings, 1)
