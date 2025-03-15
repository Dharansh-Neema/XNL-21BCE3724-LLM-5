from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from outputParser import summary_parser,ice_breaker_parser,topics_of_intrest
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model='gpt-4o',temperature=0.3)

def get_summary_chain()->RunnableSequence:
    temp= """
    Given the information from web search write {information}
    1. A short summary 
    2. Two intresting facts about them
    \n {format_instructions}
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"],
        template=temp,
        partial_variables={
            "format_instructions":summary_parser.get_format_instructions()
        })
    return summary_prompt_template | llm | summary_parser

def get_ice_breaker()->RunnableSequence:
    temp = """
        Given the information from web search  {information}
        write  2 creative Ice breakers with them that are derived from their activity
        \n{format_instructions}
        """

    ice_breaker_template = PromptTemplate(
                input_variables=["information"],
                template=temp,
                partial_variables={
                "format_instructions":ice_breaker_parser.get_format_instructions()
                })
    return ice_breaker_template | llm | ice_breaker_parser    