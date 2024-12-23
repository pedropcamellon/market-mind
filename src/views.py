from django.shortcuts import render
import logging

from src.services.agent import Agent


def search_view(request):
    global agent

    result = ""

    if request.method == "POST":
        company_name = request.POST.get("query", "")

        if not company_name:
            return render(
                request, "search.html", {"result": "Please enter a company name"}
            )

        agent = Agent()
        result = agent.get_response(company_name)
        logging.info(f"(views / search_view) Result: {result}")

    return render(request, "search.html", {"result": result})
