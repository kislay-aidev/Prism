from data.ticker_data import get_dataset, lookup, search

__all__ = ["TickerRepository", "get_repository"]


class TickerRepository:
    def search(self, query: str, limit: int = 8) -> list[dict]:
        return search(query, limit=limit)

    def lookup(self, symbol: str) -> dict | None:
        return lookup(symbol)

    def get_all(self) -> list[dict]:
        return get_dataset()


_repository: TickerRepository | None = None


def get_repository() -> TickerRepository:
    global _repository
    if _repository is None:
        _repository = TickerRepository()
    return _repository
