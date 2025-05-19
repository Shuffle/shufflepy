import os
import singul 

# Local testing from the ./singul folder:
# python3 -m pip install -e . 

singul.remove_binary()

resp = singul.run("jira", action="list_tickets", max_items=10)
print("RESP:", resp)
