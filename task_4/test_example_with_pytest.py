import pytest
import requests
from urls import *


class TestExampleWithPytest:

    @pytest.fixture(scope='class')
    def return_text(self):
        return 'Example test'

    @pytest.mark.parametrize('url', [GOOGLE, WAZUH, GITHUB])
    def test_validate_url_status_200(self, url, return_text):
        response = requests.get(url=url)

        assert response.status_code == 200, 'Not match'
        assert return_text == 'Example test', 'Not match'
