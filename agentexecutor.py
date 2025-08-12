import json
from datetime import datetime
from contractreviewagent import extract_risklabel_clauses

import os


def agent_executor(contract_text):
   
  
    try:
      
        return extract_risklabel_clauses(contract_text)
        
                 
    except Exception as e:
        print(f"Error during clause extraction: {e}")
    

if __name__ == "__main__":
    
    contract_text = """
        12. Indemnification 
        Each Party shall indemnify and hold harmless the other Party against third-party claims arising from 
        its own gross negligence or willful misconduct. 
        13. Governing Law and Dispute Resolution 
        13.1 Governing Law 
        This Agreement is governed by the laws of [Provider’s State/Country]. 
        13.2 Venue 
        Any disputes shall be resolved in the courts located in [Provider’s Jurisdiction]. 
        14. Entire Agreement 
        This Agreement, including Schedules A and B, constitutes the entire agreement between the 
        Parties and supersedes all prior understandings, whether written or oral. 
        Schedule A – Service Description (Example) 
        • Cloud-based file storage with user access controls 
        • Daily incremental backups 
        • 99.9% uptime commitment 
        • 24/7 technical support via email and chat 
        Schedule B – Pricing and Payment Terms (Example) 
        • Monthly Base Fee: $500 
        • Storage Fee: $0.10 per GB over 1 TB 
        • Payment Terms: Net 30 days 
        Signatures 
        Authorized Representative 
        ABC Cloud Store 
        Authorized Representative 
        XYZ Accounting Firm

    """     
    print(f"Extracted clauses (streaming), starting time: {datetime.now()}")

    clauses = agent_executor(contract_text)
    print(f"Extracted clauses: {clauses}")

        # Define output folder and file
    output_folder = "extracted_clauses"
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, "acme_clauses_output.json")

    # Save to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clauses, f, indent=2, ensure_ascii=False)
    
    print(f"Extracted clauses (streaming), end time: {datetime.now()}")