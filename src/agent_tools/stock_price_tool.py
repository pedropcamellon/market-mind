from langchain.tools import BaseTool
import logging
import random


class StockPriceTool(BaseTool):
    name: str = "stock_price_checker"
    description: str = "Get the current stock price for a given company"

    def _run(self, company_name: str) -> int:
        # Implement actual stock price checking logic here
        # Return random stock price
        random_price = random.randint(100, 1000)

        logging.info(f"(tools / _run) Stock price for {company_name}: {random_price}")

        return random_price
