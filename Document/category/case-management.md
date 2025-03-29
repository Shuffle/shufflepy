---
icon: folders
---

# Case Management

The **`Cases` module** in Singul allows you to manage tickets across supported tools such as **Jira**, **GitHub**, **TheHive**, and more — using unified API calls.

Whether you're creating, updating, or searching for tickets, the logic is the same: you pass a few parameters, and Singul handles the rest.

***

### Available Actions

Singul currently supports the following case/ticket actions:

| Action           | Description                            |
| ---------------- | -------------------------------------- |
| `list_tickets`   | List all tickets in a project or org   |
| `get_ticket`     | Fetch details for a single ticket      |
| `create_ticket`  | Create a new ticket or issue           |
| `update_ticket`  | Update ticket fields (summary, status) |
| `close_ticket`   | Mark a ticket as closed/resolved       |
| `add_comment`    | Add a comment to a specific ticket     |
| `search_tickets` | Search tickets using custom filters    |

***

### Usage Examples

Each method requires the following core parameters:

* `app`: Name of the connected tool (e.g. `"jira"`)
* `auth_id`: The app’s **authentication ID** from your [Shuffle dashboard](https://shuffler.io/)
* `fields`: A list of key-value dictionaries (custom inputs for each action)
* `org_id`: _(Optional)_ Your organization ID (only needed for some apps)

***

#### List Tickets

```python
response = singul.cases.list_tickets(
    app="jira",
    auth_id="YOUR_AUTH_ID"
)
```

***

#### Get Ticket Details

```python
response = singul.cases.get_ticket(
    app="jira",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "issueIdOrKey", "value": "SNT-14"}
    ]
)
```

***

#### Create Ticket

```python
response = singul.cases.create_ticket(
    app="jira",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "project", "value": "SNT"},
        {"key": "summary", "value": "Created via Singul"},
        {"key": "issuetype", "value": "Task"}
    ]
)
```

***

#### Update Ticket

```python
response = singul.cases.update_ticket(
    app="jira",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "issueIdOrKey", "value": "SNT-14"},
        {"key": "summary", "value": "Updated via API"},
        {"key": "description", "value": "Details changed"}
    ]
)
```

***

#### Add Comment to Ticket

```python
response = singul.cases.add_comment(
    app="jira",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "issueIdOrKey", "value": "SNT-14"},
        {"key": "comment", "value": "This comment was added using Singul."}
    ]
)
```

***

#### Close Ticket

```python
response = singul.cases.close_ticket(
    app="jira",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "issueIdOrKey", "value": "SNT-14"},
        {"key": "resolution", "value": "Done"}
    ]
)
```

***

#### Search Tickets

```python
response = singul.cases.search_tickets(
    app="jira",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "jql", "value": "project = SNT AND status = Open"}
    ]
)
```

***

### Best Practices

* Always test your action with known test tickets before running on production data.
* Use `search_tickets()` when you need filtered data instead of listing everything.
* Each integration (Jira, GitHub, TheHive, etc.) may expect different fields — refer to the app-specific documentation inside [Shuffle](https://shuffler.io/search?tab=apps).
