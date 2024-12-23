from googlesearch import search as google_search

class GoogleSearch:
    def process(self, query) -> tuple[int, dict]:
        """Calls the Google Custom Search API.

        Args:
        search_engine_id: The ID of the Custom Search engine.
        api_key: The API key for the Custom Search engine.
        query: The search query.

        Returns:
        A JSON object containing the results of the search.
        """

        if query is None:
            raise ValueError("Query is missing")

        results = google_search(query)

        return 200, list(results)