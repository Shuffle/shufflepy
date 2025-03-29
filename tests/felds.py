# --------------------------------------------------------------------------------------------------
# Block 1: All possible flexible message key variations
# --------------------------------------------------------------------------------------------------

SLACK_MSG_FIELDS = [
    {"key": "text", "value": "Hello from 'text' key"},
    # {"key": "msg", "value": "Hello from 'msg' key"},
    # {"key": "message", "value": "Hello from 'message' key"},
    # {"key": "body", "value": "Hello from 'body' key"},
    # {"key": "content", "value": "Hello from 'content' key"},
    # {"key": "text_message", "value": "Hello from 'text_message' key"},
    # {"key": "textBody", "value": "Hello from 'textBody' key"},
    # {"key": "Text", "value": "Hello from 'Text' (capitalized)"},
    # {"key": "msg_body", "value": "Hello from 'msg_body' key"},
    # {"key": "textual", "value": "Hello from 'textual' key"},
]

# --------------------------------------------------------------------------------------------------
# Block 2: All possible flexible channel key variations
# --------------------------------------------------------------------------------------------------

SLACK_CHANNEL_FIELDS = [
    {"key": "channel", "value": "general"},
    # {"key": "chan", "value": "general"},
    # {"key": "chn", "value": "general"},
    # {"key": "channel_name", "value": "general"},
    # {"key": "destination", "value": "general"},
    # {"key": "group", "value": "general"},
    # {"key": "to", "value": "general"},
    # {"key": "target_channel", "value": "general"},
    # {"key": "channelId", "value": "general"},
    # {"key": "Channel", "value": "general"},
]

# --------------------------------------------------------------------------------------------------
# Block 3: All possible flexible Channel key variations
# --------------------------------------------------------------------------------------------------

SLACK_CHANNEL_ID = [
    {"key": "channel_id", "value": "C0731TS09FB"},
    # {"key": "channel", "value": "C0731TS09FB"},
    # {"key": "channel id", "value": "C0731TS09FB"},
    # {"key": "chnl", "value": "C0731TS09FB"},
    # {"key": "chnel id", "value": "C0731TS09FB"},
    # {"key": "chenal id", "value": "C0731TS09FB"},
    # {"key": "chnnel", "value": "C0731TS09FB"},
]

# --------------------------------------------------------------------------------------------------
# Block 4: All possible flexible Msg search key variations
# --------------------------------------------------------------------------------------------------

SLACK_MSG_SEARCH = [
    {"key": "query", "value":"hello"},
    # {"key": "search", "value":"hello form python"},
    # {"key": "search_query", "value":"hi"},
]

# --------------------------------------------------------------------------------------------------
# Block 5: All possible flexible limit number of results key variations
# --------------------------------------------------------------------------------------------------

SLACK_LIMIT_OF_NUMBER_RESULTS = [
    {"key": "limite", "value": "100"},
    {"key": "limit number of results", "value": "3"},
    {"key": "cnt", "value": "5"},
    {"key": "cout", "value": "5"},
    {"key": "result lenth", "value": "5"},
    {"key": "resul limite", "value": "5"},
    {"key": "resul count", "value": "5"},
    {"key": "limite count", "value": "5"},
    {"key": "count of result", "value": "5"},
]

# --------------------------------------------------------------------------------------------------
# Block 6: All possible flexible key variations for the URL
# --------------------------------------------------------------------------------------------------

MALICIOUS_URLS   = [
    {"key": "domain", "value": "www.infopercept.com"},  # Malware distribution site
    # {"key": "domain", "value": "http://malicious-site.com"},  # Phishing site
    # {"key": "domain", "value": "http://example-bad-site.ru"},  # Malware distribution site
    # {"key": "domain", "value": "http://phishing-example.net"},  # Phishing site
    # {"key": "domain", "value": "http://malware-download.com"},  # Malware distribution site
    # {"key": "domain", "value": "http://fake-login-page.org"},  # Phishing site
    # {"key": "domain", "value": "http://infected-website.biz"},  # Malware distribution site
    # {"key": "domain", "value": "http://scam-site.info"},  # Scam site
    # {"key": "domain", "value": "http://dangerous-download.net"},  # Malware distribution site
    # {"key": "domain", "value": "http://fraudulent-site.co"},  # Phishing site
    # {"key": "domain", "value": "http://malicious-link.org"},  # Malware distribution site
    # {"key": "domain", "value": "http://phishing-scam.com"},  # Phishing site
    # {"key": "domain", "value": "http://harmful-site.net"},  # Malware distribution site
    # {"key": "domain", "value": "http://fake-bank-login.com"},  # Phishing site
    # {"key": "domain", "value": "http://compromised-website.org"},  # Malware distribution site
    # {"key": "domain", "value": "http://deceptive-site.info"},  # Scam site
    # {"key": "domain", "value": "http://malware-hosting.net"},  # Malware distribution site
    # {"key": "domain", "value": "http://phishing-example.co"},  # Phishing site
    # {"key": "domain", "value": "http://untrustworthy-site.com"},  # Scam site
    # {"key": "domain", "value": "http://infected-download.org"},  # Malware distribution site
]

# --------------------------------------------------------------------------------------------------
# Block 7: All possible flexible key variations for the IP
# --------------------------------------------------------------------------------------------------

MALICIOUS_IP = [
    {"key": "IP", "value": "2.207.122.217"},  # No associated hostname found
    # {"key": "IP", "value": "16.98.105.44"},   # No associated hostname found
    # {"key": "IP", "value": "23.115.181.79"},  # No associated hostname found
    # {"key": "IP", "value": "23.120.164.223"}, # No associated hostname found
    # {"key": "IP", "value": "23.125.47.174"},  # No associated hostname found
#     {"key": "IP", "value": "23.126.175.91"},  # No associated hostname found
#     {"key": "IP", "value": "24.5.186.69"},    # No associated hostname found
#     {"key": "IP", "value": "24.35.146.129"},  # No associated hostname found
#     {"key": "IP", "value": "24.35.224.134"},  # No associated hostname found
#     {"key": "IP", "value": "24.57.177.62"},   # No associated hostname found
#     {"key": "IP", "value": "24.61.51.198"},   # No associated hostname found
#     {"key": "IP", "value": "24.95.55.109"},   # No associated hostname found
#     {"key": "IP", "value": "24.96.132.245"},  # No associated hostname found
#     {"key": "IP", "value": "24.120.111.1"},   # No associated hostname found
#     {"key": "IP", "value": "24.129.34.178"},  # No associated hostname found
#     {"key": "IP", "value": "24.183.185.26"},  # No associated hostname found
#     {"key": "IP", "value": "24.207.135.38"},  # No associated hostname found
#     {"key": "IP", "value": "24.208.37.250"},  # No associated hostname found
#     {"key": "IP", "value": "24.217.244.159"}, # No associated hostname found
#     {"key": "IP", "value": "24.237.88.229"},  # No associated hostname found
#     {"key": "IP", "value": "35.142.81.169"},  # No associated hostname found
#     {"key": "IP", "value": "35.144.25.177"},  # No associated hostname found
#     {"key": "IP", "value": "35.144.33.141"},  # No associated hostname found
#     {"key": "IP", "value": "35.146.215.140"}, # No associated hostname found
#     {"key": "IP", "value": "35.146.227.131"}, # No associated hostname found
#     {"key": "IP", "value": "35.147.9.3"},     # No associated hostname found
#     {"key": "IP", "value": "35.148.176.16"},  # No associated hostname found
#     {"key": "IP", "value": "38.23.0.57"},     # No associated hostname found
#     {"key": "IP", "value": "38.133.210.59"},  # No associated hostname found
#     {"key": "IP", "value": "38.141.246.203"}, # No associated hostname found
#     {"key": "IP", "value": "38.148.40.16"},   # No associated hostname found
#     {"key": "IP", "value": "38.186.117.13"},  # No associated hostname found
#     {"key": "IP", "value": "38.189.111.85"},  # No associated hostname found
#     {"key": "IP", "value": "45.19.108.204"},  # No associated hostname found
#     {"key": "IP", "value": "45.26.143.221"},  # No associated hostname found
#     {"key": "IP", "value": "45.29.46.175"},   # No associated hostname found
#     {"key": "IP", "value": "47.13.198.155"},  # No associated hostname found
#     {"key": "IP", "value": "47.34.47.37"},    # No associated hostname found
#     {"key": "IP", "value": "47.40.38.238"},   # No associated hostname found
#     {"key": "IP", "value": "47.160.117.187"}, # No associated hostname found
#     {"key": "IP", "value": "47.186.161.22"},  # No associated hostname found
#     {"key": "IP", "value": "47.186.247.239"}, # No associated hostname found
#     {"key": "IP", "value": "47.199.247.114"}, # No associated hostname found
#     {"key": "IP", "value": "47.202.53.158"},  # No associated hostname found
#     {"key": "IP", "value": "47.205.22.225"},  # No associated hostname found
#     {"key": "IP", "value": "47.205.83.17"},   # No associated hostname found
#     {"key": "IP", "value": "47.216.157.197"}, # No associated hostname found
#     {"key": "IP", "value": "50.5.82.5"},      # No associated hostname found
#     {"key": "IP", "value": "50.35.123.101"},  # No associated hostname found
#     {"key": "IP", "value": "50.38.32.126"},   # No associated hostname found
#     {"key": "IP", "value": "50.104.167.53"},  # No associated hostname found
#     {"key": "IP", "value": "63.77.202.137"},  # No associated hostname found
#     {"key": "IP", "value": "64.24.48.252"},   # No associated hostname found
#     {"key": "IP", "value": "65.24.80.229"},   # No associated hostname found
#     {"key": "IP", "value": "65.188.226.113"}, # No associated hostname found
#     {"key": "IP", "value": "66.10.6.17"},    
]

# --------------------------------------------------------------------------------------------------
# Block 8: All possible flexible key variations for the Hash
# --------------------------------------------------------------------------------------------------

MALICIOUS_HASHES = [
    {"key": "hash", "value": "44d88612fea8a8f36de82e1278abb02f"},  # EICAR test file
    # {"key": "hash", "value": "6a8401448a5bd2b540850f811b20a66d"},  # Dridex malware sample
    # {"key": "hash", "value": "e99a18c428cb38d5f260853678922e03"},  # Example malware hash
    # {"key": "hash", "value": "c4ca4238a0b923820dcc509a6f75849b"},  # Example malware hash
    # {"key": "hash", "value": "c81e728d9d4c2f636f067f89cc14862c"},  # Example malware hash
    # {"key": "hash", "value": "eccbc87e4b5ce2fe28308fd9f2a7baf3"},  # Example malware hash
    # {"key": "hash", "value": "a87ff679a2f3e71d9181a67b7542122c"},  # Example malware hash
    # {"key": "hash", "value": "e4da3b7fbbce2345d7772b0674a318d5"},  # Example malware hash
    # {"key": "hash", "value": "1679091c5a880faf6fb5e6087eb1b2dc"},  # Example malware hash
    # {"key": "hash", "value": "8f14e45fceea167a5a36dedd4bea2543"},  # Example malware hash
    # {"key": "hash", "value": "c9f0f895fb98ab9159f51fd0297e236d"},  # Example malware hash
    # {"key": "hash", "value": "45c48cce2e2d7fbdea1afc51c7c6ad26"},  # Example malware hash
    # {"key": "hash", "value": "d3d9446802a44259755d38e6d163e820"},  # Example malware hash
    # {"key": "hash", "value": "6512bd43d9caa6e02c990b0a82652dca"},  # Example malware hash
    # {"key": "hash", "value": "c51ce410c124a10e0db5e4b97fc2af39"},  # Example malware hash
    # {"key": "hash", "value": "aab3238922bcc25a6f606eb525ffdc56"},  # Example malware hash
    # {"key": "hash", "value": "9bf31c7ff062936a96d3c8bd1f8f2ff3"},  # Example malware hash
    # {"key": "hash", "value": "c74d97b01eae257e44aa9d5bade97baf"},  # Example malware hash
    # {"key": "hash", "value": "70efdf2ec9b086079795c442636b55fb"},  # Example malware hash
    # {"key": "hash", "value": "6f4922f45568161a8cdf4ad2299f6d23"},  # Example malware hash
    # {"key": "hash", "value": "1f0e3dad99908345f7439f8ffabdffc4"},  # Example malware hash
    # {"key": "hash", "value": "98f13708210194c475687be6106a3b84"},  # Example malware hash
    # {"key": "hash", "value": "3c59dc048e8850243be8079a5c74d079"},  # Example malware hash
    # {"key": "hash", "value": "b6d767d2f8ed5d21a44b0e5886680cb9"},  # Example malware hash
    # {"key": "hash", "value": "37693cfc748049e45d87b8c7d8b9aacd"},  # Example malware hash
    # {"key": "hash", "value": "1ff1de774005f8da13f42943881c655f"},  # Example malware hash
    # {"key": "hash", "value": "8e296a067a37563370ded05f5a3bf3ec"},  # Example malware hash
    # {"key": "hash", "value": "4e732ced3463d06de0ca9a15b6153677"},  # Example malware hash
    # {"key": "hash", "value": "02e74f10e0327ad868d138f2b4fdd6f0"},  # Example malware hash
    # {"key": "hash", "value": "33e75ff09dd601bbe69f351039152189"},  # Example malware hash
    # {"key": "hash", "value": "6ea9ab1baa0efb9e19094440c317e21b"},  # Example malware hash
    # {"key": "hash", "value": "34173cb38f07f89ddbebc2ac9128303f"},  # Example malware hash
    # {"key": "hash", "value": "c16a5320fa475530d9583c34fd356ef5"},  # Example malware hash
    # {"key": "hash", "value": "6364d3f0f495b6ab9dcf8d3b5c6e0b01"},  # Example malware hash
    # {"key": "hash", "value": "182be0c5cdcd5072bb1864cdee4d3d6e"},  # Example malware hash
    # {"key": "hash", "value": "e369853df766fa44e1ed0ff613f563bd"},  # Example malware hash
    # {"key": "hash", "value": "1c383cd30b7c298ab50293adfecb7b18"},  # Example malware hash
    # {"key": "hash", "value": "19ca14e7ea6328a42e0eb13d585e4c22"},  # Example malware hash
]

# --------------------------------------------------------------------------------------------------
# Block 9: All possible flexible key variations for the Salc connetct fields
# --------------------------------------------------------------------------------------------------

SLACK_CONTACT_FIELDS = [
    {"key": "user", "value": "jenilv@infopercept.com"},
    # {"key": "email", "value": "someone@example.com"},
    # {"key": "user_id", "value": "U12345678"},
    # {"key": "userId", "value": "U12345678"},
    # {"key": "userID", "value": "U12345678"},
    # {"key": "userid", "value": "U12345678"},
    # {"key": "username", "value": "someone@example.com"},
    # {"key": "contact", "value": "someone@example.com"},
    # {"key": "contact_id", "value": "U12345678"},
]

# --------------------------------------------------------------------------------------------------
# Block 10: All possible flexible key variations for the Salc attachment fields
# --------------------------------------------------------------------------------------------------

SLACK_ATTACHMENT_FIELDS = [
    {"key": "attachment", "value": None},
    # {"key": "file_id", "value": None},
    # {"key": "fileId", "value": None},
    # {"key": "file", "value": None},
    # {"key": "attachment_id", "value": None},
    # {"key": "file_id_value", "value": None},  # hypothetical variant
]