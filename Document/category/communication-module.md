---
icon: comments
---

# Communication Module

The `Communication` module in Singul enables you to send, receive, search, and manage messages across popular platforms like **Outlook**, **Slack**, **Gmail**, **Telegram**, **Discord**, **Microsoft Teams**, and more.

You can also retrieve attachments, access contacts, and integrate messaging workflows using a unified interface.

***

### Available Actions

| Action             | Description                                     |
| ------------------ | ----------------------------------------------- |
| `list_messages`    | List recent messages from a channel/email/chat  |
| `send_message`     | Send a message to a recipient or channel        |
| `get_message`      | Retrieve a specific message                     |
| `search_messages`  | Search messages based on filters (e.g. keyword) |
| `list_attachments` | List all attachments associated with messages   |
| `get_attachment`   | Download a specific attachment                  |
| `get_contact`      | Retrieve contact information                    |

***

### Core Parameters

| Parameter | Description                                                           |
| --------- | --------------------------------------------------------------------- |
| `app`     | Messaging platform (e.g. `"slack"`, `"gmail"`, `"telegram_bot"`)      |
| `auth_id` | Authentication ID from your [Shuffle](https://shuffler.io/) dashboard |
| `fields`  | List of key-value pairs for the action input                          |
| `org_id`  | _(Optional)_ Organization ID if required by the app                   |

***

### Usage Examples

#### List Messages

```python
response = singul.communication.list_messages(
    app="slack",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "channel", "value": "general"}
    ]
)
print(response)
```

***

#### Send Message

```python
response = singul.communication.send_message(
    app="gmail",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "to", "value": "user@example.com"},
        {"key": "subject", "value": "Test Email"},
        {"key": "body", "value": "This is a test email sent via Singul."}
    ]
)
print(response)
```

***

#### Search Messages

```python
response = singul.communication.search_messages(
    app="outlook_office365",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "query", "value": "password reset"}
    ]
)
print(response)
```

***

#### Get Specific Message

```python
response = singul.communication.get_message(
    app="microsoft_teams",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "message_id", "value": "abc-123-def"}
    ]
)
print(response)
```

***

#### List Attachments

```python
response = singul.communication.list_attachments(
    app="gmail",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "email_id", "value": "xyz-456"}
    ]
)
print(response)
```

***

#### Get Attachment

```python
response = singul.communication.get_attachment(
    app="slack",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "file_id", "value": "file-789"}
    ]
)
print(response)
```

***

#### Get Contact Info

```python
response = singul.communication.get_contact(
    app="smseagle",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "contact_id", "value": "c123"}
    ]
)
print(response)
```

***

### Supported Communication Apps (Examples)

* **Outlook Office365** (`outlook_office365`)
* **Slack** (`slack`)
* **Gmail** (`gmail`)
* **Telegram Bot** (`telegram_bot`)
* **Microsoft Teams** (`microsoft_teams`)
* **Microsoft Teams User Access** (`microsoft_teams_user_access`)
* **Discord** (`discord`)
* **SMSEagle** (`smseagle`)
* **Threema Broadcast** (`threema_broadcast`)
* **Email (Generic)** (`email`)

> This list is not exhaustive. Shuffle supports many additional messaging apps.

***

### Best Practices

* Validate message IDs and channel names before sending or searching.
* Use `list_attachments()` before downloading to confirm the correct file ID.
* Ensure your app has the right OAuth scopes or permissions for messaging APIs.
