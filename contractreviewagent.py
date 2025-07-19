from ollama import chat
from pydantic import BaseModel
from typing import List

# Define the schema for a contract clause
class Clause(BaseModel):
    title: str
    text: str

class ClauseList(BaseModel):
    clauses: List[Clause]


def extract_clauses(contract_text):
    """
    Extracts contract clauses from the provided contract text using an AI model.

    Args:
        contract_text (str): The full text of the contract to analyze.

    Returns:
        List[Clause]: A list of Clause objects, each containing a title and text.

    Raises:
        pydantic.ValidationError: If the response from the model cannot be parsed into ClauseList.
        Exception: If there is an error communicating with the Ollama API.
    """

    
    # Define the system prompt for clause extraction
    system_prompt = (
        "You are a Contract Review assistant! Need a JSON list with each clause clearly indicated, "
        "present each as a JSON object with 'title' and 'text'. "
        "Reminder: Output only the answer, nothing else."
    )
    
    # Combine the system prompt with the contract text
    full_prompt = f"{system_prompt}\n\nContract Text:\n{contract_text}\n\nExtracted Clauses:"
    
    # Query the Ollama API to get the response
    stream_response = chat(
        model='llama3.1:8b',       
        messages=[{'role': 'user', 'content': full_prompt}],
        format=ClauseList.model_json_schema(),
        stream=True,      
    )

        # Collect streamed chunks
    chunks = []
    for chunk in stream_response:
        # Each chunk is a partial message (string)
        chunks.append(chunk.message.content)
        # Optionally, print(chunk, end="", flush=True)  # For real-time display

    # Combine all chunks into a single string
    full_response = "".join(chunks)
    
    # Parse and validate the structured response
    response = ClauseList.model_validate_json(full_response)
    
    return response.clauses

