


def create_product_json(name, description, price, category_id, category_name):

    data = {
        "name": name,
        "description": description,
        "price": price,
        "category_id": category_id,
        "category_name": category_name
    }
    return data


def update_product_json(id, name, description, price, category_id):

    data = {
        "id": id,
        "name": name,
        "description": description,
        "price": price,
        "category_id": category_id
    }
    return data


def delete_product_json(id):

    data = {
        "id": id
    }
    return data
