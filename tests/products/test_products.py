import pytest
from endponits.product import Product
from json_modules import products_json


@pytest.mark.run(order=1)
def test_get_product(app_config):
    product = Product()
    all_products = product.request_products(app_config.base_url, 200)
    product.check_products_data_by_length(all_products, 18)
    print(all_products.text)


@pytest.mark.run(order=2)
def test_create_product_1(app_config):
    product = Product()
    product_info = products_json.create_product_json(
        "Gainer Max Power",
        "This product consists of natural ingredients and is super effective for skinny guys.",
        99.00,
        4,
        "Supplements"
    )
    response = product.create_product(app_config.base_url, product_info, 201)
    product.success_message_for_product_created(response)
    all_products = product.request_products(app_config.base_url, 200)
    product.check_products_data_by_length(all_products, 19)


@pytest.mark.run(order=3)
def test_create_product_2(app_config):
    product = Product()
    product_info = products_json.create_product_json(
        "Tracksuit",
        "This tracksuits provide is capable of enduring cold weather.",
        85.00,
        3,
        "Active Wear - Unisex"
    )
    response = product.create_product(app_config.base_url, product_info, 201)
    product.success_message_for_product_created(response)
    all_products = product.request_products(app_config.base_url, 200)
    product.check_products_data_by_length(all_products, 20)


@pytest.mark.run(order=4)
def test_get_new_product_1(app_config):
    product = Product()
    all_products = product.request_products(app_config.base_url, 200)
    new_product = product.get_item_by_name(all_products, "Gainer Max Power")
    print(new_product)


@pytest.mark.run(order=5)
def test_get_new_product_2(app_config):
    product = Product()
    all_products = product.request_products(app_config.base_url, 200)
    new_product = product.get_item_by_name(all_products, "Tracksuit")
    print(new_product)


@pytest.mark.run(order=6)
def test_update_new_product_1(app_config):
    product = Product()
    id = product.get_product_id(app_config.base_url, "Gainer Max Power")
    updated_data = products_json.update_product_json(id, "Gainer Superman", "Only for supermen.", 89.00, 1)
    response = product.update_product(app_config.base_url, updated_data, 200)
    product.success_message_for_product_updated(response)


@pytest.mark.run(order=7)
def test_update_new_product_2(app_config):
    product = Product()
    id = product.get_product_id(app_config.base_url, "Tracksuit")
    updated_data = products_json.update_product_json(id, "Hoodie", "Warmer than the tracksuit.", 89.00, 3)
    response = product.update_product(app_config.base_url, updated_data, 200)
    product.success_message_for_product_updated(response)


@pytest.mark.run(order=8)
def test_delete_product_1(app_config):
    product = Product()
    id = product.get_product_id(app_config.base_url, "Gainer Superman")
    json_id = products_json.delete_product_json(id)
    response = product.delete_product(app_config.base_url, json_id, 200)
    all_products = product.request_products(app_config.base_url, 200)
    product.check_products_data_by_length(all_products, 19)
    product.success_message_for_product_deleted(response)


@pytest.mark.run(order=9)
def test_delete_product_2(app_config):
    product = Product()
    id = product.get_product_id(app_config.base_url, "Hoodie")
    json_id = products_json.delete_product_json(id)
    response = product.delete_product(app_config.base_url, json_id, 200)
    all_products = product.request_products(app_config.base_url, 200)
    product.check_products_data_by_length(all_products, 18)
    product.success_message_for_product_deleted(response)
