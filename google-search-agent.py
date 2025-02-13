from phi.agent import Agent;
from phi.model.groq import Groq;
from phi.tools.googlesearch import GoogleSearch;
from dotenv import load_dotenv;

load_dotenv()

web_search_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    tools=[GoogleSearch()],
    description="You are a lead finder that helps users find potential website development clients",
    instructions=[
        "Given a service business category and the location by a user, respond with 10 business in that location",
        "Select businesses with only 4 or less than 4 star ratings on their google listing and provide their website links and star ratings",
        "Search in English",
    ]
)

web_search_agent.print_response("category is house keeping service and location is melbourne, VIC, Australia", markdown=True)