import pytest
from ingestion.coingecko_api import get_coin_list


def test_fetch_coins_success(mocker):
    # Mock response data
    mock_data = [
        {"id": "bitcoin", "symbol": "btc", "current_price": 50000}
    ]

    # Mock requests.get
    mock_response = mocker.Mock()
    mock_response.json.return_value = mock_data
    mock_response.raise_for_status.return_value = None

    mocker.patch("ingestion.coingecko_api.requests.get", return_value=mock_response)

    result = get_coin_list()

    assert isinstance(result, list)
    assert result[0]["id"] == "bitcoin"
    
    
def test_fetch_coins_api_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = Exception("API error")

    mocker.patch("ingestion.coingecko_api.requests.get", return_value=mock_response)

    with pytest.raises(Exception):
        get_coin_list()
        

def test_fetch_coins_empty_response(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = []
    mock_response.raise_for_status.return_value = None

    mocker.patch("ingestion.coingecko_api.requests.get", return_value=mock_response)

    result = get_coin_list()

    assert result == []