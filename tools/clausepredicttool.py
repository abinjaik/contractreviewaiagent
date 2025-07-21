import joblib


def predict_clause_risk(text):
    try:
        model = joblib.load("tools/regressionmodeltrainer/clause_text_classifier.joblib")
        pred = model.predict([text])[0]
        return pred
    except FileNotFoundError:
        print("Model file not found. Please ensure 'msa_text_classifier.joblib' exists.")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None



def label_clause(clause_text: str,clause_title:str) -> str:
    """
    Predicts the risk label for a given clause text using an AI model.
    
    Args:
        clause_text (str): The text of the clause to analyze.
        clause_title (str): The title of the clause for context.
    Returns:
        str: The predicted risk label for the clause.
    """
    # Call the AI model to predict the risk label
    response = predict_clause_risk(clause_title + clause_text)
    
    # Return the predicted label
    return response if response else "unknown"

# 2. Tools schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "label_clause",
            "description": "Review clause for labelling severity.",
            "parameters": {
                "type": "object",
                "properties": {
                    "clause_text": {"type": "string"},
                    "clause_title": {"type": "string"}                     
                },
                "required": ["clause_text", "clause_title"]
            }
        }
    }
]

if __name__ == "__main__":
    # Example usage
    clause_text = "Client waives any right to withhold payment for defective or incomplete work."
    clause_title = "Fees and Payment"
    
    label = label_clause(clause_text, clause_title)
    print(f"Predicted label for the clause '{clause_title}': {label}")