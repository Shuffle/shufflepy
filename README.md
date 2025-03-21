# Shufflepy
Connect to your favorite services with a single line of code. 

**This Library is in an Experimental Phase, [released under pypi](https://pypi.org/project/shufflepy/)**

## Installation
```bash
pip install shufflepy
```

## Configuration
```python
from shufflepy import Singul 

## If the config is not specified, the library will use `https://shuffler.io` as the default URL. You must specify an apikey. 

shuffle = Singul(
	"APIKEY",
	url='https://shuffler.io',
)
```

## Requirements
- [An API-key for Shuffle](https://shuffler.io/settings)
- Having an active authentication for the service you are trying to connect to in Shuffle, whether in your own instance or in the Shuffle cloud: [https://shuffler.io](https://shuffler.io/admin?tab=app_auth). This will be added to the future Shuffle CLI, and is also doable with the [App Authentication API](https://shuffler.io/docs/API#add-app-authentication). 
- **If onprem**: [A Shuffle instance](https://github.com/shuffle/shuffle).

## Usage
Sample functions below. If none of these match, try to use the shuffle.connect() function to run ANYTHING. By default returns the [matching translation standard](https://github.com/Shuffle/standards/tree/main/translation_standards) if available, otherwise the raw output.
```python
shuffle.cases.create_ticket("jira", title="Title")
shuffle.communication.send_message("slack", message="Test")
shuffle.communication.send_message("teams", message="Test")
tickets = shuffle.cases.list_tickets("jira")
```

**Normal App run control:**
```python
shuffle.run_app(app_id="bc78f35c6c6351b07a09b7aed5d29652", action="repeat_back_to_me", params={"call": "The value to repeat"})
```

## Manual:
```python
# General connect
resp = shuffle.cases.list_tickets(
	app="jira",
	org_id=os.environ.get("SHUFFLE_ORG_ID"),
	fields=[{
		"key": "max-amount",
		"value": "10"
	}]
)

print(resp)

# General transformer - Transforms from any data into a standard, e.g. "list_tickets"
sourcedata = [{"title": "Tickettitle", "id": "hiya"}]
tickets = shuffle.transform(sourcedata, "list_tickets") # (coming soon)

print(tickets)
```

Basic output for `list_tickets`: 
```json
[{
  "id": "P-123",
  "title": "Ticket 1"
},
{
  "id": "P-124",
  "title": "Ticket 2"
}]
```

[See default standards](https://github.com/Shuffle/standards/blob/main/translation_standards) - Standards are modifiable, and you will see your own standards on the [File page in Shuffle](https://shuffler.io/admin?tab=files).

## Exploring usage
To look through past executions, see the execution debugger available on [/workflows/debug](https://shuffler.io/workflows/debug)
<img width="1150" alt="image" src="https://github.com/user-attachments/assets/c0b3d28f-897e-47d1-9f79-d195e5682824">


## Available Apps & categories
- [>2500 APIs: Search in Shuffle](https://shuffler.io/search?tab=apps)

## Available Categories (May 2024)
- Ticket management 	(Cases)
- Communication/Email	(Comms)
- SIEM 					(SIEM)	
- EDR/XDR 				(Eradication)
- Asset Management  	(Assets)
- Identity				(IAM) 
- Threat Intel			(Intel)
- Cloud Security		(Cloud)