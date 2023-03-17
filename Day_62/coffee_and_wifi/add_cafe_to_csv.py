import csv

class AddCafe():

    def __init__(self, form):
        self.cafe_name = form.cafe.data
        self.map_link = form.map_link.data
        self.open = form.open.data
        self.close = form.close.data
        self.coffee = form.coffee.data
        self.wifi = form.wifi.data
        self.power = form.power.data
        self.cafe_data = [
            form.cafe.data,
            form.map_link.data,
            form.open.data,
            form.close.data,
            form.coffee.data,
            form.wifi.data,
            form.power.data
        ]

    def add_to_csv(self, the_csv):
        with open(the_csv, "a", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(self.cafe_data)