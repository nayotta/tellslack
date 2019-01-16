workflow "Send message to slack" {
  on = "push"
  resolves = ["Tell Slack"]
}

action "Tell Slack" {
  uses = "./tell_slack"
  secrets = ["SLACK_TOKEN", "SLACK_CHANNEL"]
}
