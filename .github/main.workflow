workflow "New workflow" {
  on = "push"
  resolves = ["./tell_slack"]
}

action "./tell_slack" {
  uses = "./tell_slack"
  secrets = ["SLACK_TOKEN", "SLACK_CHANNEL"]
}
