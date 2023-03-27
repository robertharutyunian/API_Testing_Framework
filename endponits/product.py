from base.base_api import BaseApi


get_all_products_endpoint = "api_testing/product/read.php"
create_product_endpoint = "api_testing/product/create.php"
update_product_endpoint = "api_testing/product/update.php"
delete_product_endpoint = "api_testing/product/delete.php"

class Product(BaseApi):


    def request_products(self, url, expected_status_code):

        """
        :param url: This is the base url for the request.
        :param expected_status_code: The status code that should return after the request is made.
        :return: Returns the response.
        """

        response = self.get_request(url+get_all_products_endpoint)
        assert self.status_code_is_correct(response, expected_status_code), "Status codes do not match."
        return response


    def check_products_data_by_length(self, response, expected_length):

        """
        :param response: The response that we get after a request is made.
        :param expected_length: The number of products that should be returned after the request is made.
        :return:
        """

        actual_length = self.get_length_of_data(response)
        assert actual_length == expected_length, "The lengths of the items do not match."


    def create_product(self, url, product_info, expected_status_code):

        """
        :param url: This is the base url for the request.
        :param product_info: The json data that will go into the body of the requests.
        :param expected_status_code: The status code that we will get after successfully creating the product.
        :return: Returns the response.
        """

        response = self.post_request(url+create_product_endpoint, product_info)
        assert self.status_code_is_correct(response, expected_status_code), "Status codes do not match."
        return response


    def success_message_for_product_created(self, response):
        """

        :param response: The response that we get after a request is made.
        :return:
        """

        assert "Product was created." in response.text, "The response message does not match."


    def update_product(self, url, updated_data, expected_status_code):
        """

        :param url: The base url.
        :param updated_data: The json data that we want to update on the product.
        :param expected_status_code: The status code that we will get after successfully updating the product.
        :return:
        """

        response = self.put_request(url+update_product_endpoint, updated_data)
        assert self.status_code_is_correct(response, expected_status_code),  "The status codes do not match."
        return response


    def get_product_id(self, url, name):
        """

        :param url: The base url in order to make a reqeust.
        :param name: The product name of which we would like to get the id from.
        :return: The product id.
        """

        all_products = self.get_request(url+get_all_products_endpoint)
        product = self.get_item_by_name(all_products, name)
        return product[0]["id"]


    def success_message_for_product_updated(self, response):
        """

        :param response: The response that we get after a request is made.
        :return:
        """

        assert "Product updated" in response.text, "The response message does not match."


    def delete_product(self, url, product_id, expected_status_code):
        """

        :param url: The base url in order to make a reqeust.
        :param product_id: The product id in json format.
        :param expected_status_code: The status code that we will get after successfully deleting the product.
        :return:
        """

        response = self.delete_request(url+delete_product_endpoint, product_id)
        assert self.status_code_is_correct(response, expected_status_code)
        return response


    def success_message_for_product_deleted(self, response):
        """

        :param response: The response that we get after a request is made.
        :return:
        """

        assert "Product was deleted" in response.text, "The response message does not match."
