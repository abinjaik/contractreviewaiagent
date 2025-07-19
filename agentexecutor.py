import json
from datetime import datetime
from contractreviewagent import extract_clauses



def agent_executor(contract_text):
    """
    Extracts clauses from a contract text and prepares them for further processing.

    Parameters:
        contract_text (str): The full text of the contract to be analyzed.

    Returns:
        list: A list of dictionaries, each containing information about an extracted clause.

    Workflow:
        1. Extracts clauses from the contract text using the extract_clauses function.
        2. Attempts to parse the extraction output as JSON; if parsing fails, falls back to a naive split.
        3. (Commented out) Optionally classifies the severity of each clause.
    """
    # Step 1: Extract clauses using Llama 3.1
    extraction_output = extract_clauses(contract_text)  
    
    # Try to parse JSON output; if not, implement a parser for your prompt format
    try:
              
        clauses = extraction_output
        
    except Exception:
        # Fallback: naive split (for demo), replace with robust parsing
        clauses = [{"title": "Clause", "text": c.strip()} for c in extraction_output.split('\n\n') if c.strip()]
    
    # Step 2: Classify severity for each clause using BERT
    # for clause in clauses:
    #     clause['severity'] = classify_severity(clause['text'])
    return clauses

if __name__ == "__main__":
    
    contract_text = """
    This Master Service Agreement (“Agreement”) is made effective as of July 1, 2025 (the “Effective Date”) by and between: • Provider: ABC Cloud Store, with its principal place of business at [Provider Address]. • Client: XYZ Accounting, with its principal place of business at [Client Address]. ABC Cloud Store and XYZ Accounting may be referred to individually as a “Party” or collectively as the “Parties.” 1. Purpose This Agreement sets forth the terms and conditions under which ABC Cloud Store shall provide cloud-based data storage and related services to XYZ Accounting. 2. Definitions • “Services” means the cloud-based storage, data management, and related technical support described in Schedule A. • “Client Data” means all data or content provided by XYZ Accounting to ABC Cloud Store for storage or processing. 3. Term This Agreement shall commence on the Effective Date and continue for an initial term of 24 months (the “Initial Term”), unless terminated earlier as provided herein. Upon expiration of the Initial Term, this Agreement shall automatically renew for successive 12 month periods unless either Party provides at least 60 days’ prior written notice of non-renewal. 4. Fees and Payment 4.1 Fees XYZ Accounting shall pay ABC Cloud Store the fees described in Schedule B (Pricing and Payment Terms). 4.2 Invoicing and Payment ABC Cloud Store will invoice monthly in advance. Payments are due within 30 days of invoice date.
    """
    print(f"Contract Agent starting time: {datetime.now()}")
    results = agent_executor(contract_text)  
    print(f"Contract Agent ending time: {datetime.now()}")  
    for clause in results:
        print(f"Title: {clause.title}\nText: {clause.text}\n")
