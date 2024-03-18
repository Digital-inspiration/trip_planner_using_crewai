from crewai import Task
from textwrap import dedent

"""
Creating Tasks cheatsheet:
- Begin with the end in mind. Identify the specific outccome your tasks are aiming tot achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itenary for the trip including city selection, attractions, and practical advice.

Key Steps for Task creation:
1. Identify the desired outcome: Define what success looks like for your project.
    - A detailed 7 day travbel itinerary.

2. Task breakdown: Divide the goal into smalled, manageable tasks that agents can execute.
    - itinerary Planning: develop a detailed plan for each day of the trip
    - City Selection: Analyze and pick the best cities to visit.
    - Local Tour Guide: Pick the best local expert to provide insights and recommendations.

3. Assign Tasks to agents: Match tasks with agents based on their roles and expertise.


4. Task description template:
    - Use this template as a guide to define each task in your CrewAi applicaiton.
    - This template helps ensure that each task is clearly defined, actionable, and aligned with your goal.

Template:
---------
def [task_name](self, agent, [parameters]):
    return Task(
        description=dedent(f''' 
            ***Task***: [Provide a concise name or summary of your task.]
            ***Description****: [Detailed description of what the agent is expected to do, including any actionable steps and examples.]

        ***Parameters***:
        -[Parameter 1]: [Description]
        -[Parameter 2]: [Description]
        ...Add more as required

        **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, adiitional rewards.]

        '''), agent=agent
        )
        
    )
"""

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Task**: Develop a 7 day travel itinerary
                **Description**: Expand the city guide into a full 7-day travel itinerary with detailed 
                per day plans, including weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                and actual restaurents to go to. This itinerary should cover all aspects of the trip, 
                from arrival to departure, integrating the city guide information with practical travel losgistics.

                **Parameters**:
                City: {city}
                Trip dates: {travel_dates}
                Traveller interests:{interests}
            
                **Note**: {self.__tip_section()}
    
                Make sure to use the most recent data as possible.
    
        """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the best city for the trip.
            **Description**: Analyze and select the best city 
            for the trip based on specific criteria such as weather patterns, 
            seasonal trends, and travel preferences and travel costs. 
            This task involves comparing multiple cities m considering factors 
            like current weather conditions, upcoming cultural or seasonal events 
            and overall travel expenses. Your final answer must be a detailed report 
            on the chosen city, including actual flight cost from the origin city, 
            weather forecasts and attractions.
            
            **Parameters**:
            - Origin: {origin}
            - Cities: {cities}
            - Interests: {interests}
            - Trip dates: {travel_dates}

            **Notes**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def gather_city_info(self, agent, city, interests, travel_dates):
            return Task(
                description=dedent(
                    f"""
                **Task**: Gather in-depth city guide information.
                **Description**: Compile an in-depth guide for the selected city,
                including detailed information about the city's local customs, 
                special events and daily activity recommendations. This guide should 
                provide a thorough overvie of what the city has to offer, 
                including hidden gems, cultural hubspots, must-visit landmarks and 
                weather forecasts, and a high level cost of travel.

                **Parameters**:
                - City: {city}
                - Interests: {interests}
                - Trip dates: {travel_dates}       

                **Notes**: {self.__tip_section()}
            """
                ),
                agent=agent,
            )
