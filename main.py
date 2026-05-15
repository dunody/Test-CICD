import os
from dotenv import load_dotenv

# Get a env variable
load_dotenv()
CID = os.environ['CID']
print(f"{CID} => len {len(CID)}")

for i in CID:
    print(i)