---
icon: shield
---

# SIEM Integration

The `SIEM` module in Singul allows you to manage alerts and detections across supported tools such as **Wazuh**, **Elastic Search**, **Splunk**, **Microsoft Sentinel**, **QRadar**, and more — using unified API calls.

Whether you're listing alerts, searching logs, or isolating endpoints, the process is simple: pass a few parameters, and Singul does the rest.

***

### Available Actions

Singul currently supports the following SIEM actions:

| Action               | Description                                        |
| -------------------- | -------------------------------------------------- |
| `list_alerts`        | List all alerts from the connected SIEM            |
| `get_alert`          | Get details for a specific alert                   |
| `close_alert`        | Close or mark an alert as resolved                 |
| `search`             | Run custom queries (e.g. by agent, rule, severity) |
| `create_detection`   | Create a detection rule or manual alert            |
| `add_to_lookup_list` | Add an IP, domain, or hash to a lookup/block list  |
| `isolate_endpoint`   | Isolate a machine/host from the network            |

***

### Core Parameters

Each method requires the following parameters:

| Parameter | Description                                                           |
| --------- | --------------------------------------------------------------------- |
| `app`     | Name of the SIEM tool (e.g. `"wazuh"`, `"splunk"`, `"sentinel"`)      |
| `auth_id` | Authentication ID from your [Shuffle](https://shuffler.io/) dashboard |
| `fields`  | List of key-value pairs specific to the action                        |
| `org_id`  | _(Optional)_ Your organization ID (used by some apps)                 |

***

### Usage Examples

#### List Alerts

```python
response = singul.siem.list_alerts(
    app="wazuh",
    auth_id="YOUR_AUTH_ID"
)
print(response)
```

***

#### Get Alert by ID

```python
response = singul.siem.get_alert(
    app="wazuh",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "alert_id", "value": "12345"}
    ]
)
print(response)
```

***

#### Close an Alert

```python
response = singul.siem.close_alert(
    app="wazuh",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "alert_id", "value": "12345"},
        {"key": "reason", "value": "Resolved via automation"}
    ]
)
print(response)
```

***

#### Search Alerts

```python
response = singul.siem.search(
    app="wazuh",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "query", "value": "agent.name: server-01 AND rule.level: >10"}
    ]
)
print(response)
```

***

#### Create Detection Rule

```python
response = singul.siem.create_detection(
    app="wazuh",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "rule_name", "value": "High CPU usage"},
        {"key": "rule_level", "value": "12"}
    ]
)
print(response)
```

***

#### Isolate Endpoint

```python
response = singul.siem.isolate_endpoint(
    app="wazuh",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "agent_id", "value": "001"},
        {"key": "reason", "value": "Malicious activity detected"}
    ]
)
print(response)
```

***

#### Add to Lookup List

```python
response = singul.siem.add_to_lookup_list(
    app="wazuh",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "type", "value": "ip"},
        {"key": "value", "value": "192.168.1.100"},
        {"key": "list", "value": "blocklist"}
    ]
)
print(response)
```

***

### Best Practices

* Test all SIEM actions with known alert data before using them in automation
* Use `search()` with targeted queries to avoid overloading the response
* Field formats vary between apps — check Shuffle's in-app schema for accurate keys
