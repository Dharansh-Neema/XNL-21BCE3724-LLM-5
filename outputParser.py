from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import List,Dict,Any
from logger import setup_logger
logger = setup_logger(name="OutputParser")

class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    def to_dict(self) -> Dict[str, Any]:
        try:
            logger.debug("Summary output parser returned")
            return {"summary": self.summary, "facts": self.facts}
        except Exception as e:
            logger.error("Unexceted error occurred while returning Summary output parser".e)
            raise e

class IceBreaker(BaseModel):
    ice_breakers: List[str] = Field(description="ice breaker list")

    def to_dict(self) -> Dict[str, Any]:
        try:
            return {"ice_breakers": self.ice_breakers}
        except Exception as e:
            logger.error("Unexceted error occurred while returning IceBreaker output parser",e)
            raise e


class TopicOfInterest(BaseModel):
    topics_of_interest: List[str] = Field(
        description="topic that might interest the person"
    )

    def to_dict(self) -> Dict[str, Any]:
        try:
            return {"topics_of_interest": self.topics_of_interest}
        except Exception as e:
            logger.error("Unexceted error occurred while returning TopicOfInterest output parser",e)
            raise e

summary_parser = PydanticOutputParser(pydantic_object=Summary)
ice_breaker_parser = PydanticOutputParser(pydantic_object=IceBreaker)
topics_of_intrest = PydanticOutputParser(pydantic_object=TopicOfInterest)