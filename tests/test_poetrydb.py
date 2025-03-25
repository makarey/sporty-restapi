import pytest
import logging
import requests

from core.base_test import BaseTest


class TestPoetryDB(BaseTest):

    @pytest.mark.poetry
    def test_get_all_authors(self, api_url):
        """
        Test the API endpoint for retrieving all authors.

        This test verifies the following:
        - The API endpoint returns a 200 status code.
        - The response is a JSON object (dictionary).
        - The JSON object contains a key named 'authors'.
        - The 'authors' key contains a list.
        - The list of authors is not empty.

        Args:
            api_url (str): The base URL of the API under test.

        Raises:
            AssertionError: If any of the above conditions are not met.
        """
        logging.info("Starting test to get all authors")

        url = f"{api_url}/author"
        response = requests.get(url)

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        json_data = response.json()
        assert isinstance(json_data, dict), "Response is not a dictionary"
        assert "authors" in json_data, "Key 'authors' is missing in response"
        assert isinstance(json_data["authors"], list), "'authors' key does not contain a list"
        assert len(json_data["authors"]) > 0, "Authors list is empty"


    @pytest.mark.poetry
    def test_get_poems_by_author(self, api_url):
        """
        Test the API endpoint for retrieving poems by a specific author.
        This test sends a GET request to the `/author/{author}` endpoint and verifies
        the response to ensure it meets the expected structure and data integrity.
        Args:
            api_url (str): The base URL of the API being tested.
        Assertions:
            - The response status code is 200.
            - The response body is a list.
            - Each poem in the response contains the keys: 'title', 'author', 'lines', and 'linecount'.
            - The 'author' field in each poem matches the requested author.
        """
        logging.info("Starting test to get poems by author")

        author = "William Shakespeare"
        url = f"{api_url}/author/{author}"
        response = requests.get(url)
        
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        json_data = response.json()
        assert isinstance(json_data, list), "Response is not a list"
        for poem in json_data:
            assert "title" in poem, "Missing 'title' key in poem object"
            assert "author" in poem, "Missing 'author' key in poem object"
            assert "lines" in poem, "Missing 'lines' key in poem object"
            assert "linecount" in poem, "Missing 'linecount' key in poem object"
            assert poem["author"] == author, f"Unexpected author: {poem['author']}"


    @pytest.mark.poetry
    def test_get_random_poem(self, api_url):
        """
        Test the API endpoint for retrieving a random poem.
        This test verifies the following:
        - The API returns a 200 status code.
        - The response is a list.
        - The list contains exactly one poem.
        - The poem object contains the required keys: 'title', 'author', 'lines', and 'linecount'.
        Args:
            api_url (str): The base URL of the API being tested.
        Raises:
            AssertionError: If any of the above conditions are not met.
        """
        logging.info("Starting test to get a random poem")

        url = f"{api_url}/random"
        response = requests.get(url)
        
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        json_data = response.json()
        assert isinstance(json_data, list), "Response is not a list"
        assert len(json_data) == 1, "Response does not contain exactly one poem"
        poem = json_data[0]
        assert "title" in poem, "Missing 'title' key in poem object"
        assert "author" in poem, "Missing 'author' key in poem object"
        assert "lines" in poem, "Missing 'lines' key in poem object"
        assert "linecount" in poem, "Missing 'linecount' key in poem object"


    @pytest.mark.poetry
    def test_get_poem_by_title(self, api_url):
        """
        Test case for retrieving a poem by its title from the PoetryDB API.
        This test sends a GET request to the PoetryDB API with a specific poem title
        and verifies the following:
        - The response status code is 200 (OK).
        - The response data is a list.
        - Each poem in the response has a title that matches the requested title (case-insensitive).
        Args:
            api_url (str): The base URL of the PoetryDB API.
        Raises:
            AssertionError: If any of the assertions fail, such as unexpected status code,
                            response not being a list, or mismatched poem titles.
        """
        logging.info("Starting test to get a poem by title")

        title = "Ozymandias"
        url = f"{api_url}/title/{title}"
        response = requests.get(url)
        
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        json_data = response.json()
        assert isinstance(json_data, list), "Response is not a list"
        for poem in json_data:
            assert poem["title"].lower() == title.lower(), f"Unexpected title: {poem['title']}"


    @pytest.mark.poetry
    def test_get_poems_by_linecount(self, api_url):
        """
        Test the API endpoint for retrieving poems by line count.

        This test sends a GET request to the `/linecount/{linecount}` endpoint
        and verifies the following:
        - The response status code is 200.
        - The response data is a list.
        - Each poem in the response has a "linecount" field matching the requested line count.

        Args:
            api_url (str): The base URL of the API under test.

        Raises:
            AssertionError: If any of the assertions fail.
        """
        logging.info("Starting test to get poems by linecount")

        linecount = 14
        url = f"{api_url}/linecount/{linecount}"
        response = requests.get(url)

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        json_data = response.json()
        assert isinstance(json_data, list), "Response is not a list"
        for poem in json_data:
            assert int(poem["linecount"]) == linecount, f"Unexpected linecount: {poem['linecount']}"
