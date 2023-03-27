from base.base_api import BaseApi


get_category_endpoint = "api_testing/category/read.php"
update_category_endpoint = "api_testing/category/update.php"


class Categories(BaseApi):


    def get_categories(self, url, expected_status_code, expected_name):
        """

        :param url: The base url.
        :param expected_status_code: The status code that we should get after making the response.
        :param expected_name: The category name through which we will assert the get response result.
        :return: Returns the response.
        """

        response = self.get_request(url+get_category_endpoint)
        assert self.status_code_is_correct(response, expected_status_code)
        print(response.text)
        category_name_list = self.check_json_value_by_key(response, "$.records..name")
        expected_value = self.get_value_from_list(category_name_list, expected_name)
        assert expected_value == expected_name, "The expected category name was not found in the response."
        return response


    def update_categories(self, url, updated_data, expected_status_code):
        """

        :param url: The base url.
        :param updated_data: The json data that should be sent with the request in order to update the product.
        :param expected_status_code: The status code that we should get after making the response.
        :return:
        """

        response = self.put_request(url+update_category_endpoint, updated_data)
        assert self.status_code_is_correct(response, expected_status_code)
        return response


    def success_message_for_category_created(self, response):
        """

        :param response: The response that we get after a request is made.
        :return:
        """

        assert "Category updated" in response.text, "The response message does not match."




