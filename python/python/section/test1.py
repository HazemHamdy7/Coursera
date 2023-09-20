menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}


# def calculate_subtotal(order):
#     subtotal = sum(item["price"] for item in order)
#     return subtotal


def cal (order):
    subtotal= sum(item["price"]for item in order )
    return subtotal



    