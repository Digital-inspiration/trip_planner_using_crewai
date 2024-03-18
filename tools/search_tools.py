import json
import os
import requests
from langchain.tools import tool

# from langchain_community.utilities import GoogleSerperAPIWrapper

from dotenv import load_dotenv

load_dotenv()


class SearchTools:

    @tool("Search the internet")
    def search_internet(query):
        """
        Searches the internet for the given query/topic and return relevant results
        """
        top_result_to_return = 4
        print("Searching the internet for: ", query)
        serper_api_key = os.getenv("SERPER_API_KEY")

        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": serper_api_key,
            "Content-Type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        
        # check if there is an oraganic key
        if "organic" not in response.json():
            return "Sorry I couldn't find any relevant results, there could be an error with your serper api"
        else:
            results = response.json()["organic"]
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append(
                        "\n".join(
                            [
                                f"Title: {result['title']}",
                                f"Link: {result['link']}",
                                f"Snippet: {result['snippet']}",
                            ]
                        )
                    )
                except KeyError:
                    next
            return "\n".join(string)
