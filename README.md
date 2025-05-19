# Shufflepy ( and Singulpy
Connect to your favorite services with a Singul line of code. 

This documentation will help you get started with Singul, understand its capabilities, and integrate it into your workflows easily. Whether you're a developer, a security analyst, or an automation engineer — **Singul is built for you.**

**Singul** is an API handler that allows you to get or update data in tools like Jira, Outlook, Gmail, Service Now, and more - with a single line of code.

## Usage
Sample functions below. If none of these match, try to use the shuffle.connect() function to run ANYTHING. By default returns the [matching translation standard](https://github.com/Shuffle/standards/tree/main/translation_standards) if available, otherwise the raw output.
```python
from shufflepy import Singul 

# If you want to use REMOTE singul (shuffler.io / open source Shuffle)
singul = Singul(
	"APIKEY",
	url='https://shuffler.io',
)

singul.cases.create_ticket("jira", title="Title")
singul.communication.send_message("slack", message="Test")
singul.communication.send_message("teams", message="Test")
tickets = singul.cases.list_tickets("jira")


# If you want to run it 100% locally
resp = singul.run("jira", action="list_tickets")
```

**Normal App run control:**
```python
singul.run_app(app_id="bc78f35c6c6351b07a09b7aed5d29652", action="repeat_back_to_me", params={"call": "The value to repeat"})
```

## Manual:
```python
# General connect
resp = singul.cases.list_tickets(
	app="jira",
	org_id=os.environ.get("SHUFFLE_ORG_ID"),
	fields=[{
		"key": "max-amount",
		"value": "10"
	}]
)

### Common Use Cases

# General transformer - Transforms from any data into a standard, e.g. "list_tickets"
sourcedata = [{"title": "Tickettitle", "id": "hiya"}]
tickets = singul.transform(sourcedata, "list_tickets") # (coming soon)

* Send emails using **Outlook or Gmail**
* Fetch and manage tickets from **Jira, GitHub, or TheHive**
* Pull alerts from **SIEM or SOAR platforms**
* Automate security investigations
* Trigger workflow actions across tools
* Build lightweight automation using simple APIs

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

## Local testing
```bash
cd build_singul
cp -r ../shufflepy singul
python3 -m pip install -e . --break-system-packages

# You can now import the library locally :)
```
