#!/usr/bin/env python3.7

import json
import os
import http
from urllib import request

event_file = os.environ.get("GITHUB_EVENT_PATH")
log_file = os.environ.get("LOG_FILE")

workflow = os.environ.get("GITHUB_WORKFLOW")
repo = os.environ.get("GITHUB_REPOSITORY")
sha = os.environ.get("GITHUB_SHA")

slack_token = os.environ.get("SLACK_TOKEN")
channel = os.environ.get("SLACK_CHANNEL")

if not slack_token or not channel:
    print("SLACK_TOKEN or SLACK_CHANNEL not defined")

with open(event_file) as f:
    event = json.load(f)
    message = event["head_commit"]["message"]
    commit_url = event["head_commit"]["url"]
    repo_url = event["repository"]["url"]

    sender_name = event["sender"]["login"]
    sender_avatar_url = event["sender"]["avatar_url"]

if log_file:
    with open(log_file) as f:
        log = f.read()
else:
    log = ""

req = request.Request("https://slack.com/api/chat.postMessage")
req.add_header("Authorization", "Bearer " + slack_token)
req.add_header("Content-type", "application/json")
req.add_header("Charset", "UTF-8")

post_data = json.dumps({
    "channel": channel,
    "attachments": [
        {
            "fallback": "workflow status",
            "color": "#000000",
            "author_name": sender_name,
            "author_icon": sender_avatar_url,
            "title": "Workflow <" + repo_url + "/actions|" + workflow + "> of " + repo + "@" + sha[:7],
            "text": log,
        }
    ]
})

with request.urlopen(req, data=post_data.encode()) as res:
    print("Status:", res.status, res.reason)
    print("Data:", res.read().decode("utf-8"))
