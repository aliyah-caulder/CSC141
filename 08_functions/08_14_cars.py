# Defines a function to build a dictionary for car information including two positional arguments and one arbitrary keywword arg.

def make_car(manufacturer, model, **car_info):
    """Build a dictionary with car information"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model

    return car_info

car = make_car('jeep', 'patriot', color='red', radio=True)
print(car)