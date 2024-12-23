from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI
from langgraph.prebuilt import create_react_agent
import logging
import os
import vertexai

from ..agent_tools.stock_price_tool import StockPriceTool
from ..agent_tools.company_info_tool import CompanyInfoTool

load_dotenv()


class Agent:
    def __init__(self):
        self.agent = None
        self.setup_agent()

    def setup_agent(self):
        vertexai.init(
            project=os.getenv("GCP_PROJECT_ID"),
            location=os.getenv("GCP_PROJECT_LOCATION"),
        )

        chat_model = ChatVertexAI(model="gemini-1.5-flash-001")

        # Initialize tools
        tools = [
            StockPriceTool(),
            CompanyInfoTool(),
        ]

        # Create the agent
        self.agent = create_react_agent(
            chat_model,
            tools,
        )

    def get_prompt(self, company_name):
        return (
            f"You are an economic journalist. You have been assigned to summarize the latest"
            f"news about a company. The name of the company is '{company_name}'."
            f"Provide a paragraph summarizing the latest news about the company and its latest stock price."
        )

    def get_response(self, company_name):
        try:
            query = self.get_prompt(company_name)
            response = self.agent.invoke({"messages": [HumanMessage(content=query)]})
            messages_raw = response["messages"]
            return messages_raw[-1].content
        except Exception as e:
            logging.error(f"Error invoking agent: {e}")
