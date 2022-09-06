import pytest
from assertpy import assert_that
from api_client.Order import OrderApi


@pytest.fixture()
def order_api():
    return OrderApi()


def test_create_order():
    response = order_api.create_order()
    assert_that(response["data"]["order_status"]).is_equal_to("New")
    assert_that(response["data"]["last_updated_timestamp"]).is_not_empty()