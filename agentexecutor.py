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
                        8.2 License
                        Client grants ABC Cloud Store a non-exclusive license to host, store, and process Client Data solely to provide the Services, subject to Section 5.

                        9. Warranties and Disclaimers

                        9.1 Mutual Warranties
                        Each Party represents it has the power and authority to enter into this Agreement.

                        9.2 Provider Warranty
                        ABC Cloud Store warrants that Services will substantially conform to the Service Description in Schedule A.

                        9.3 Disclaimer
                        Except as expressly stated, ABC Cloud Store disclaims all other warranties, express or implied, including merchantability or fitness for a particular purpose.

                        10. Termination

                        10.1 Provider Termination Right
                        ABC Cloud Store may terminate this Agreement at any time, with 30 days’ prior written notice, at its sole discretion and for any reason.

                        10.2 Client Termination Restriction
                        XYZ Accounting may not terminate this Agreement except with ABC Cloud Store’s express written consent, which may be withheld for any reason or no reason at all.

                        10.3 Effect of Termination
                        Termination shall not affect ABC Cloud Store’s rights under Section 5 to retain and use XYZ Accounting Data indefinitely.

                        11. Limitation of Liability

                        11.1 Liability Cap
                        Except for indemnification obligations and breach of confidentiality, each Party’s liability shall not exceed the total fees paid in the 12 months prior to the claim.

                        11.2 Exclusion of Damages
                        Neither Party shall be liable for indirect, incidental, or consequential damages arising out of this Agreement.
                    """

    print(f"Extracted clauses , starting time: {datetime.now()}")

    clauses = agent_executor(contract_text)
    #print(f"Extracted clauses: {clauses}")

        # Define output folder and file
    output_folder = "extracted_clauses"
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, "acme_clauses_output.json")

    # Save to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clauses, f, indent=2, ensure_ascii=False)
    
    print(f"Extracted clauses (streaming), end time: {datetime.now()}")