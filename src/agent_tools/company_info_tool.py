from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.tools import BaseTool
from src.services.google_search import GoogleSearch
import logging


class CompanyInfoTool(BaseTool):
    name: str = "company_info_getter"
    description: str = "Get latest news about a company from the web"

    def _run(self, company_name: str) -> str:
        try:
            search = GoogleSearch()
            status, results_urls = search.process(f"{company_name} news")

            # Top 3 search results
            print(status, results_urls[:3])

            # Load the web page
            loader_multiple_pages = WebBaseLoader(results_urls[:3])

            documents: list[Document] = loader_multiple_pages.load()

            logging.info(f"Loaded {len(documents)} documents")

            embeddings_model = VertexAIEmbeddings(model_name="text-embedding-005")

            logging.info(f"Loaded embeddings model. Model: {embeddings_model}")

            db = FAISS.from_documents(documents, embeddings_model)

            relevant_docs = db.search(
                f"{company_name} news", search_type="similarity", k=3
            )

            context = "\n\n".join([doc.page_content for doc in relevant_docs])

            print(f"(tools / _run) Context: {context}")

            return context

        except Exception as e:
            logging.error(f"(tools / _run) Error: {e}")
            return ""
