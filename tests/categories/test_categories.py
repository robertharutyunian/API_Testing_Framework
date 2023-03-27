import pytest
from endponits.categories import Categories
from json_modules import categories_json


@pytest.mark.run(order=1)
def test_get_category(app_config):
    category = Categories()
    category.get_categories(app_config.base_url, 200, "Active Wear - Women")


@pytest.mark.run(order=2)
def test_update_categories(app_config):
    category = Categories()
    updated_data = categories_json.update_product_json(1, "Passive Wear", "The name says it all.")
    response = category.update_categories(app_config.base_url, updated_data, 200)
    category.success_message_for_category_created(response)
