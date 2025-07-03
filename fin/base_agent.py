# fin/base_agent.py

from abc import ABC, abstractmethod
from openai_utils import get_openai_response
import yfinance as yf

class BaseAgent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_response(self, user_question: str) -> str:
        prompt = f"You are the {self.name}, a specialized {self.description}. Answer the following question in a clear, concise, and expert manner: '{yf.Search(user_question)}'"
        
        return get_openai_response(prompt)

    @classmethod
    @abstractmethod
    def get_agent_name(cls) -> str:
        """Returns the name of the agent class."""
        pass

    @abstractmethod
    def get_capabilities(self) -> list[str]:
        pass

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"