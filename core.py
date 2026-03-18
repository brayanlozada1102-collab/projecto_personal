"""
Core business logic for the Sales Registration System.
All functions use dictionaries and tuples exclusively.
"""

def add_customer(customer_id, name, email, customers_dict):
    """
    Registers a new customer into the storage dictionary.
    :param customer_id: Unique string/int ID
    :param name: Customer full name
    :param email: Customer email address
    :param customers_dict: Existing customers dictionary
    :return: Updated dictionary with the new customer
    """
    new_data = {customer_id: (name, email)}
    return {**customers_dict, **new_data}

def add_product(product_id, name, price, products_dict):
    """
    Registers a new product using an immutable tuple.
    :param product_id: Unique identifier
    :param name: Product name
    :param price: Unit price (float)
    :param products_dict: Existing products dictionary
    :return: Updated dictionary containing the product tuple
    """
    product_data = (product_id, name, price)
    new_entry = {product_id: product_data}
    return {**products_dict, **new_entry}

def create_order(order_id, c_id, p_id, qty, customers, products, orders):
    """
    Creates a new order and calculates the total automatically.
    :return: Updated orders dictionary
    """
    # Get unit price from the product tuple (index 2)
    unit_price = products[p_id][2]
    total = unit_price * qty
    
    # Structure: {order_id: (customer_id, product_id, quantity, total)}
    order_data = (c_id, p_id, qty, total)
    return {**orders, **{order_id: order_data}}

def calculate_daily_income(orders_dict):
    """
    Sums all totals from the registered orders.
    :param orders_dict: Dictionary of all orders
    :return: Float representing total income
    """
    total_income = 0.0
    for o_id in orders_dict:
        total_income += orders_dict[o_id][3] # Index 3 is total_pedido
    return total_income

def get_formatted_report(customers, products, orders):
    """
    Consolidates data for the final report.
    :return: A tuple containing (total_orders, total_money)
    """
    total_revenue = calculate_daily_income(orders)
    count = len(orders)
    return (count, total_revenue)
