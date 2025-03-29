---
icon: shield-check
---

# Eradication Module

The `Eradication` module in Singul allows you to identify, investigate, and remediate threats directly through integrated EDR and SIEM platforms such as **Microsoft Defender**, **SentinelOne**, **Elastic Security**, **Carbon Black**, **Trend Micro**, and more.

It provides a unified API to perform actions like isolating hosts, blocking hashes, closing alerts, and more across multiple security platforms.

***

### Available Actions

Singul currently supports the following eradication actions:

| Action              | Description                                 |
| ------------------- | ------------------------------------------- |
| `list_alerts`       | List all alerts across connected apps       |
| `get_alert`         | Fetch details of a specific alert           |
| `close_alert`       | Mark an alert as resolved                   |
| `create_detection`  | Create a detection or trigger in the tool   |
| `block_hash`        | Block a file/hash on the endpoint           |
| `search_hosts`      | Search for hosts or endpoints               |
| `isolate_host`      | Isolate a host from the network             |
| `unisolate_host`    | Reconnect a previously isolated host        |
| `trigger_host_scan` | Initiate a malware or system scan on a host |

***

### Core Parameters

Each method accepts the following parameters:

| Parameter | Description                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------- |
| `app`     | Name of the eradication tool (e.g. `"sentinelone"`, `"bitdefender"`, `"microsoft365_defender"`) |
| `auth_id` | Authentication ID from [Shuffle](https://shuffler.io/)                                          |
| `fields`  | List of key-value pairs for the action input                                                    |
| `org_id`  | _(Optional)_ Organization ID if required by the app                                             |

***

### Usage Examples

#### List Alerts

```python
response = singul.eradication.list_alerts(
    app="microsoft365_defender",
    auth_id="YOUR_AUTH_ID"
)
print(response)
```

***

#### Get Alert Details

```python
response = singul.eradication.get_alert(
    app="sentinelone",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "alert_id", "value": "abc123"}
    ]
)
print(response)
```

***

#### Close an Alert

```python
response = singul.eradication.close_alert(
    app="elastic_security",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "alert_id", "value": "abc123"},
        {"key": "reason", "value": "Resolved via playbook"}
    ]
)
print(response)
```

***

#### Block a Hash

```python
response = singul.eradication.block_hash(
    app="trend_micro_vision_one",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "hash", "value": "d41d8cd98f00b204e9800998ecf8427e"}
    ]
)
print(response)
```

***

#### Search Hosts

```python
response = singul.eradication.search_hosts(
    app="bitdefender",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "hostname", "value": "endpoint-22"}
    ]
)
print(response)
```

***

#### Isolate a Host

```python
response = singul.eradication.isolate_host(
    app="huntress",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "hostname", "value": "webserver-1"},
        {"key": "reason", "value": "C2 communication detected"}
    ]
)
print(response)
```

***

#### Unisolate a Host

```python
response = singul.eradication.unisolate_host(
    app="carbon_black_response",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "hostname", "value": "webserver-1"}
    ]
)
print(response)
```

***

#### Trigger Host Scan

```python
response = singul.eradication.trigger_host_scan(
    app="withsecure_elements",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "hostname", "value": "finance-pc"}
    ]
)
print(response)
```

***

### Supported Eradication Apps (Examples)

Below is a sample of supported eradication tools. Many others are also available via Shuffle:

* **Microsoft 365 Defender** (`microsoft365_defender`)
* **SentinelOne** (`sentinelone`)
* **Elastic Security** (`elastic_security`)
* **Carbon Black Response** (`carbon_black_response`)
* **Trend Micro Vision One** (`trend_micro_vision_one`)
* **BitDefender** (`bitdefender`)
* **WithSecure Elements** (`withsecure_elements`)
* **FortiEDR** (`fortiedr`)
* **Cylance** (`cylance`)
* **Huntress** (`huntress`)

> These are just examples. Singul supports many more eradication tools via Shuffle's integration catalog.

***

### Best Practices

* Always confirm alert and host identifiers before performing critical actions.
* Isolate hosts only when verified threat indicators are confirmed.
* Use `block_hash()` for proactive blocking of known malware signatures.
* Combine `create_detection()` with automated scanning for high-confidence response.
