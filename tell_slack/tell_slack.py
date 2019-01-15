#!/usr/bin/env python3.7

import json
import os
import http
from urllib import request, parse

event_file = os.environ["GITHUB_EVENT_PATH"]
log_file = os.environ["LOG_FILE"]

workflow = os.environ["GITHUB_WORKFLOW"]
repo = os.environ["GITHUB_REPOSITORY"]
sha = os.environ["GITHUB_SHA"]

slack_token = os.environ["SLACK_TOKEN"]
channel = os.environ["SLACK_CHANNEL"]

with open(event_file) as f:
    event = json.load(f)
    message = event["head_commit"]["message"]
    commit_url = event["head_commit"]["url"]
    repo_url = event["repository"]["url"]

with open(log_file) as f:
    log = f.read()

text = "[%s](%s)@[%s](%s) %s\n%s: %s" % (repo, repo_url, sha[:7],
                                         commit_url, message.split("\n", 1)[0], workflow, log)

req = request.Request("https://slack.com/api/chat.postMessage")
req.add_header("Authorization", "Bearer " + slack_token)
req.add_header("Content-type", "application/json")

post_data = parse.urlencode([
    ("channel", channel),
    ("text", "hello world"),
])

with request.urlopen(req, data=post_data.encode('utf-8')) as res:
    print('Status:', res.status, res.reason)
    print('Data:', res.read().decode('utf-8'))
