# openai_utils.py
from openai import AzureOpenAI
import config

def get_openai_response(prompt):
    """
    Calls the Azure OpenAI API to get a response from the GPT-4o model.
    """
    try:
        client = AzureOpenAI(
            api_key=config.AZURE_OPENAI_API_KEY,
            api_version=config.AZURE_OPENAI_API_VERSION,
            azure_endpoint=config.AZURE_OPENAI_ENDPOINT
        )

        response = client.chat.completions.create(
            model=config.AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful and knowledgeable financial assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred while calling OpenAI API: {e}")
        return f"An error occurred while generating the response: {e}"