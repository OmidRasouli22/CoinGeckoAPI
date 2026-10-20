import pytest
from ingestion.coingecko_api import get_coin_list


def test_fetch_coins_success(mocker):
    # Mock response data
    mock_data = [
        {"id": "bitcoin", "symbol": "btc", "current_price": 50000}
    ]

    # Mock requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data

    mocker.patch("ingestion.coingecko_api.requests.get", return_value=mock_response)

    result = get_coin_list()

    assert isinstance(result, list)
    assert result[0]["id"] == "bitcoin"
    
    
def test_fetch_coins_api_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500

    mocker.patch("ingestion.coingecko_api.requests.get", return_value=mock_response)

    with pytest.raises(Exception):
        get_coin_list()
        

def test_fetch_coins_empty_response(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = []

    mocker.patch("ingestion.coingecko_api.requests.get", return_value=mock_response)

    result = get_coin_list()

    assert result == []


def test_fetch_coins_retries_when_rate_limited(mocker):
    limited = mocker.Mock(status_code=429)
    ok = mocker.Mock(status_code=200)
    ok.json.return_value = [{"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"}]

    get = mocker.patch("ingestion.coingecko_api.requests.get", side_effect=[limited, ok])
    sleep = mocker.patch("ingestion.coingecko_api.time.sleep")

    result = get_coin_list()

    assert result[0]["id"] == "bitcoin"
    assert get.call_count == 2
    sleep.assert_called_once_with(1)
