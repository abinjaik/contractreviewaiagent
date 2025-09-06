from ollama import chat
from pydantic import BaseModel,TypeAdapter
from typing import List
from tools.clausepredicttool import tools, label_clause

# Define the schema for a contract clause
class Clause(BaseModel):
    title: str
    text: str
    label: str = None  # Optional label for classification

class ClauseList(BaseModel):
    clauses: List[Clause]







def extract_risklabel_clauses(contract_text):
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
        "present each as a JSON object with 'title', 'text' and 'label "       
    )
    
    # Combine the system prompt with the contract text
    full_prompt = f"{system_prompt}\n\nContract Text:\n{contract_text}\n\nExtracted Clauses:"
    
    messages = [{'role': 'user', 'content': full_prompt}]
    # Query the Ollama API to get the response
    response = chat(
        model='llama3.1:8b',       
        messages=messages,        
        tools=tools,    
    )

    labeled_clauses:List[Clause] = []
        # Collect streamed chunks
    if hasattr(response.message, "tool_calls") and response.message.tool_calls:        
        tool_calls = response.message.tool_calls
        for tool_call in tool_calls:
            tool_name = tool_call["function"]["name"]
            
            arguments = tool_call["function"]["arguments"]

            clause_text = arguments.get('clause_text', '')
            clause_title = arguments.get('clause_title', '')
            
            # Parse args safely (usually a JSON string)
            import json
            args = json.loads(clause_text) if isinstance(arguments, str) else arguments

            # Call matching Python function
            if tool_name == "label_clause":
                result = label_clause(**args)                
                labeled_clauses.append(Clause(title=clause_title, text=clause_text, label=result))
                indicator = "\033[91mNegative\033[91m"  if result.endswith('negative') else "\033[94mPositive\033[94m"    
                print(f"\033[92mTool call detected: {tool_name}, Title={clause_title},\033[0m Label={ indicator}")
        ClauseListAdapter = TypeAdapter(ClauseList)
        # Serialize to JSON (returns bytes)
        
        json_bytes = ClauseListAdapter.dump_json(labeled_clauses)
        json_str = json_bytes.decode("utf-8")
        
        return  json_str  
               
    else:
        print("No tool call detected.")

