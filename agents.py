
from textwrap import dedent
from crewai import Agent
from langchain.llms import Ollama
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

"""
Creating Agents cheatsheet:
- Think like a boss. Work backwards from the goal ans think which employee you need to hire to get the job done.
- Define the Captain of the crew who orient the otehr agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.
- Think of which tools the captain/experts needs to use to get the job done.

Build a top down structure of the crew

Goal:
- Create a 7 day travel itinerary with detailed per day plans, including budget, packing suggeswtions and safety tips.

Captain/Manager/Boss:
- Expert travel agent 

Employees/Exxperts to hire:
- City selection expert
- Local tour guide

Notes:
- Agents should be results friven and have a clear goal in mind
- Role is their job title
- Goals should be actionable
- Backstory is their resume
"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistic. I have decades of experience makeing travel itinerary"""),
            goal=dedent(f"""
                        Create a 7 day itinerary plan with detailed per day plan,
                         including budget, activities to do, packing suggesstions
                         and also safety tips
                        """),
            tools=[SearchTools.search_internet,
                   CalculatorTools.calculate],
            verbose=True,
            llm=self.Ollama,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices and traveller interests"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.Ollama,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city, its history, its attractions and local customs"""),
            goal=dedent(f"""Provide the best insights about the selected city"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.Ollama,
        )
