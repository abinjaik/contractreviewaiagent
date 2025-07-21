import json
from datetime import datetime
from contractreviewagent import extract_risklabel_clauses




def agent_executor(contract_text):
   
  
    try:
      
        return extract_risklabel_clauses(contract_text)
        
                 
    except Exception as e:
        print(f"Error during clause extraction: {e}")
    

if __name__ == "__main__":
    
    contract_text = """
    This Master Service Agreement (“Agreement”) is made effective as of July 1, 2025 (the “Effective Date”) by and between: • Provider: ABC Cloud Store, with its principal place of business at [Provider Address]. • Client: XYZ Accounting, with its principal place of business at [Client Address]. ABC Cloud Store and XYZ Accounting may be referred to individually as a “Party” or collectively as the “Parties.” 1. Purpose This Agreement sets forth the terms and conditions under which ABC Cloud Store shall provide cloud-based data storage and related services to XYZ Accounting. 2. Definitions • “Services” means the cloud-based storage, data management, and related technical support described in Schedule A. • “Client Data” means all data or content provided by XYZ Accounting to ABC Cloud Store for storage or processing. 3. Term This Agreement shall commence on the Effective Date and continue for an initial term of 24 months (the “Initial Term”), unless terminated earlier as provided herein. Upon expiration of the Initial Term, this Agreement shall automatically renew for successive 12 month periods unless either Party provides at least 60 days’ prior written notice of non-renewal. 4. Fees and Payment 4.1 Fees XYZ Accounting shall pay ABC Cloud Store the fees described in Schedule B (Pricing and Payment Terms). 4.2 Invoicing and Payment ABC Cloud Store will invoice monthly in advance. Payments are due within 30 days of invoice date.
    """     
    print(f"Extracted clauses (streaming), starting time: {datetime.now()}")

    clauses = agent_executor(contract_text)
    print(f"Extracted clauses: {clauses}")
    
    print(f"Extracted clauses (streaming), end time: {datetime.now()}")