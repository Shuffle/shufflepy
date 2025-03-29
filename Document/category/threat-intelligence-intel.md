---
icon: brain-circuit
---

# Threat Intelligence (Intel)

The `Intel` module in Singul enables you to fetch, search, manage, and enrich IOCs (Indicators of Compromise) across popular threat intel platforms such as **MISP**, **Shodan**, **AbuseIPDB**, **GreyNoise**, **OpenCTI**, **VirusTotal**, and more.

Whether you're pulling IOC details, searching based on threat attributes, or managing enrichment workflows, the API remains consistent.

***

### Available Actions

| Action       | Description                                        |
| ------------ | -------------------------------------------------- |
| `get_ioc`    | Retrieve details about a specific IOC              |
| `search_ioc` | Search threat intelligence using a filter or query |
| `create_ioc` | Create a new IOC in the connected platform         |
| `update_ioc` | Update an existing IOC                             |
| `delete_ioc` | Delete or remove an IOC from the system            |

***

### Core Parameters

Each method accepts the following parameters:

| Parameter | Description                                                                     |
| --------- | ------------------------------------------------------------------------------- |
| `app`     | Name of the threat intel tool (e.g. `"misp"`, `"virustotal_v3"`, `"greynoise"`) |
| `auth_id` | Authentication ID from [Shuffle](https://shuffler.io/) dashboard                |
| `fields`  | List of key-value pairs specific to the action                                  |
| `org_id`  | _(Optional)_ Your organization ID if required by the app                        |

***

### Usage Examples

#### Get IOC

```python
response = singul.intel.get_ioc(
    app="virustotal_v3",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "hash", "value": "44d88612fea8a8f36de82e1278abb02f"}
    ]
)
print(response)
```

***

#### Search IOC

```python
response = singul.intel.search_ioc(
    app="greynoise",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "ip", "value": "8.8.8.8"}
    ]
)
print(response)
```

***

#### Create IOC

```python
response = singul.intel.create_ioc(
    app="misp",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "type", "value": "ip-src"},
        {"key": "value", "value": "45.77.23.1"},
        {"key": "comment", "value": "IOC from external alert feed"}
    ]
)
print(response)
```

***

#### Update IOC

```python
response = singul.intel.update_ioc(
    app="opencti_dcon",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "ioc_id", "value": "ioc-abc-123"},
        {"key": "tags", "value": "APT29, critical"}
    ]
)
print(response)
```

***

#### Delete IOC

```python
response = singul.intel.delete_ioc(
    app="abuseipdb_v2",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "ioc_id", "value": "ioc-abc-123"}
    ]
)
print(response)
```

***

### Supported Threat Intelligence Apps (Examples)

Here are some of the popular platforms Singul supports in the Intel module:

* **MISP** (`misp`)
* **AbuseIPDB v2** (`abuseipdb_v2`)
* **Shodan** (`shodan`)
* **GreyNoise** (`greynoise`)
* **OpenCTI dcon** (`opencti_dcon`)
* **Falcon Sandbox Public API** (`falcon_sandbox_public_api`)
* **VirusTotal v3** (`virustotal_v3`)
* **Hudson Rock Cavalier** (`hudson_rock_cavalier`)
* **AlienvaultOTX** (`alienvaultotx`)
* **IBM X-Force** (`ibm_x-force`)

> Many more platforms are supported. This list is just a starting point.

***

### Best Practices

* Use `search_ioc()` for fast lookups during investigations.
* Always validate supported field keys in Shuffle’s in-app schema viewer.
* Avoid storing full hashes or PII in public IOC repositories.
