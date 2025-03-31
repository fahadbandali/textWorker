from typing import Dict
from openai import AsyncOpenAI

class OpenAIClientWrapper:
    def __init__(self, api_Key) -> None:
        self.client = AsyncOpenAI(api_key=api_Key)
        
    async def prompt(self, arg) -> Dict[str, str]:
        response = await self.client.responses.create(
            model="gpt-4o-mini",
            input=arg,
            tools=[]
        )

        return { "response": response.output_text }
    
    