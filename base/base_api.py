import json
import requests
import jsonpath as jsn


class BaseApi:


    def get_request(self, url, params=None, headers=None):

        """
        Use this method to send the get request
        :param url: The reqeust URL
        :param params: The request params (OPTIONAL)
        :param headers: The request headers (OPTIONAL)
        :return:
        """

        response = requests.get(url, params=params, headers=headers, verify=False)
        return response


    def post_request(self, url, json):

        """
        :param url: The request URL
        :param json: The request body
        :return:
        """

        response = requests.post(url, json=json, verify=False)
        return response


    def put_request(self, url, json):

        """
        :param url: The reqeust URL
        :param json: The new data
        :return:
        """
        response = requests.put(url, json=json, verify=False)
        return response


    def delete_request(self, url, json):

        """
        :param url: The request URL
        :return:
        """

        response = requests.delete(url, json=json, verify=False)
        return response


    def status_code_is_correct(self, response, expected_status_code):

        """
        To check the response code
        :param response:
        :param expected_status_code:
        :return:
        """

        return response.status_code == expected_status_code


    def check_json_value_by_key(self, response, key, value=None):
        json_data = json.loads(response.text)
        values_in_json = jsn.jsonpath(json_data, key)
        return values_in_json


    def get_value_from_list(self, values_list, expected_value):
        for val in values_list:
            if val == expected_value:
                return val


    def get_length_of_data(self, response):

        """
        :param response: The response that we get after the request.
        :return: The number of items that we receive after the request.
        """

        json_data = json.loads(response.text)
        return len(json_data["records"])


    def get_item_by_name(self, response, name):
        """

        :param response: The response that we get after the request.
        :param name: The item name for getting the item object.
        :return: Return the item object.
        """

        json_data = json.loads(response.text)
        current_item = jsn.jsonpath(json_data, f"$.records[?(@.name == '{name}')]")
        return current_item
