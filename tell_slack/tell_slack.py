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

if log_file:
    with open(log_file) as f:
        log = f.read()
else:
    log = None

text = "[%s](%s)@[%s](%s) %s" % (repo, repo_url, sha[:7],
                                 commit_url, message.split("\n", 1)[0])
if log:
    text += "\n%s: %s" % (workflow, log)

req = request.Request("https://slack.com/api/chat.postMessage")
req.add_header("Authorization", "Bearer " + slack_token)
req.add_header("Content-type", "application/json")
req.add_header("Charset", "UTF-8")

post_data = json.dumps({
    "channel": channel,
    "text": text,
    "mrkdwn": True,
})

with request.urlopen(req, data=post_data.encode()) as res:
    print("Status:", res.status, res.reason)
    print("Data:", res.read().decode("utf-8"))
