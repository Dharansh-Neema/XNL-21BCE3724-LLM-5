from logger import setup_logger
from dotenv import load_dotenv
from tavily import TavilyClient
import os
load_dotenv()
logger = setup_logger(name="tools")
def get_profile_url(name:str)->str:
    try:
        """Search for the Linkdien profile and return a url"""
        client = TavilyClient(os.getenv("TAVILY_API_KEY"))
        result = client.search(name)
        # print(result)
        logger.debug("Tools search executed successfully")
        return result
    except Exception as e:
        logger.error("Error occurred while executing the tool search ",e)
        raise
