import json
import os

import pytest
import config
from app_factory import create_app

@pytest.fixture()
def app():
    app = create_app(config.TestConfig)
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


defined_date = {"date": "2022-01-02"}


def test_total_sales_value(client):
    response = client.get("/v1/total_sales_value/7842cf43-28f7-4a85-9d74-1be87663bdf6",
                          query_string=defined_date,
                          headers={"X-Api_Key": os.getenv("TEST_API_KEY")})
    assert response.status_code == 200
    assert json.loads(response.data) == {'date': '2022-01-02', 'store_id': '7842cf43-28f7-4a85-9d74-1be87663bdf6'}