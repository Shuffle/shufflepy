---
icon: computer
---

# Asset Management

The `Assets` module in Singul enables you to query, retrieve, and search for information about assets, users, endpoints, and vulnerabilities across various connected platforms like **Active Directory**, **Vicarius**, **Snipe-IT**, **Rapid7**, **Device42**, **Axonius**, **AWS**, and more.

Singul provides a unified API layer that abstracts all asset-related actions, so you don't need to write platform-specific code.

***

### Available Actions

Singul currently supports the following asset-related actions:

| Action                   | Description                                       |
| ------------------------ | ------------------------------------------------- |
| `list_assets`            | List all available assets from the connected app  |
| `get_asset`              | Fetch detailed information about a specific asset |
| `search_assets`          | Search for assets based on filters                |
| `search_users`           | Search for user-related assets                    |
| `search_endpoints`       | Search for endpoint assets or host machines       |
| `search_vulnerabilities` | Search for asset vulnerabilities                  |

***

### Core Parameters

Each method accepts the following parameters:

| Parameter | Description                                                                     |
| --------- | ------------------------------------------------------------------------------- |
| `app`     | Name of the app (e.g. `"snipeit"`, `"device42"`, `"rapid7_insightvm"`)          |
| `auth_id` | The app's authentication ID from your [Shuffle](https://shuffler.io/) dashboard |
| `fields`  | List of key-value pairs specific to the action                                  |
| `org_id`  | _(Optional)_ Your organization ID if required by the app                        |

***

### Usage Examples

#### List All Assets

```python
response = singul.assets.list_assets(
    app="snipeit",
    auth_id="YOUR_AUTH_ID"
)
print(response)
```

***

#### Get a Specific Asset

```python
response = singul.assets.get_asset(
    app="snipeit",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "asset_id", "value": "123"}
    ]
)
print(response)
```

***

#### Search Assets

```python
response = singul.assets.search_assets(
    app="device42",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "hostname", "value": "db-server"}
    ]
)
print(response)
```

***

#### Search Users

```python
response = singul.assets.search_users(
    app="activedirectory",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "username", "value": "jdoe"}
    ]
)
print(response)
```

***

#### Search Endpoints

```python
response = singul.assets.search_endpoints(
    app="axonius",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "ip_address", "value": "10.0.0.15"}
    ]
)
print(response)
```

***

#### Search Vulnerabilities by CVE, Vendor & Model

```python
response = singul.assets.search_vulnerabilities(
    app="rapid7_insightvm",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "cve", "value": "CVE-2023-12345"},
        {"key": "vendor", "value": "Cisco"},
        {"key": "model", "value": "RV340"}
    ]
)
print(response)
```

> You can use any combination of `cve`, `vendor`, and `model` to narrow your vulnerability search.

***

### Best Practices

* Use `search_*` methods with targeted filters to limit result sizes.
* Match field names to what the app expects — you can find these in Shuffle's app schema.
* Test actions with known asset IDs or usernames before full automation.
