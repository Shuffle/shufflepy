---
icon: cube
---

# Other Module

The `Other` module in Singul is a flexible category that provides utility and system-level operations for various tools that don't strictly fit into other standard modules like SIEM, IAM, or Communication. These actions range from retrieving configs, health checks, system information, and even executing remote scripts.

This module is ideal for working with tools like **Wazuh**, **Shuffle Tools**, **Webroot**, **HTTP APIs**, **Nmap**, **Veeam**, and more.

***

### Available Actions

| Action                | Description                                             |
| --------------------- | ------------------------------------------------------- |
| `update_info`         | Update system or app metadata                           |
| `get_info`            | Retrieve general information from the connected app     |
| `get_status`          | Check current system or service status                  |
| `get_version`         | Get version info for a service or platform              |
| `get_health`          | Fetch application or service health metrics             |
| `get_config`          | Get configuration for a component                       |
| `get_configs`         | Get a list of all available configs                     |
| `get_configs_by_type` | Filter configs by type (e.g., network, agents, logging) |
| `get_configs_by_name` | Filter configs by name                                  |
| `run_script`          | Run a remote script or command                          |

***

### Core Parameters

| Parameter | Description                                                       |
| --------- | ----------------------------------------------------------------- |
| `app`     | Name of the tool (e.g. `"wazuh"`, `"shuffle_tools"`, `"webroot"`) |
| `auth_id` | Authentication ID from [Shuffle](https://shuffler.io/) dashboard  |
| `fields`  | List of key-value pairs for input values                          |
| `org_id`  | _(Optional)_ Your organization ID if required by the app          |

***

### Usage Examples

#### Get System Info

```python
response = singul.other.get_info(
    app="shuffle_tools",
    auth_id="YOUR_AUTH_ID"
)
print(response)
```

***

#### Update Metadata

```python
response = singul.other.update_info(
    app="http",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "info_key", "value": "version"},
        {"key": "value", "value": "v2.0.1"}
    ]
)
print(response)
```

***

#### Get Health Status

```python
response = singul.other.get_health(
    app="wazuh",
    auth_id="YOUR_AUTH_ID"
)
print(response)
```

***

#### Get Configs by Type

```python
response = singul.other.get_configs_by_type(
    app="logicmonitor_rest__bearer_2",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "type", "value": "collectors"}
    ]
)
print(response)
```

***

#### Run Script

```python
response = singul.other.run_script(
    app="shuffle",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "script", "value": "echo Hello from Shuffle"}
    ]
)
print(response)
```

***

### Supported Apps (Examples)

* **Wazuh** (`wazuh`)
* **Shuffle Tools** (`shuffle_tools`)
* **HTTP APIs** (`http`)
* **Nmap Scan** (`nmap_scan`)
* **Webroot** (`webroot`)
* **Veeam Backup & Replication** (`veeam_backup__replication_re`)
* **LogicMonitor REST API** (`logicmonitor_rest__bearer_2`)
* **Abnormal Security** (`abnormal_security`)
* **Abmex Test App** (`abmex_teste`)

> Many of these tools provide health, status, script, or config APIs that are ideal for this module.

***

### Best Practices

* Use `get_status()` or `get_health()` in regular monitoring flows.
* `run_script()` is powerful — use with care and proper permissions.
* Use `get_configs_by_type()` and `get_configs_by_name()` to dynamically audit or modify system configurations.
