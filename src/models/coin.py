class Coin:
    """
    Simple internal Coin object used in the application.

    """

    def __init__(self, id: str, symbol: str, name: str):
        self.id = id
        self.symbol = symbol
        self.name = name

    def __repr__(self):
        return f"Coin(id={self.id}, symbol={self.symbol}, name={self.name})"