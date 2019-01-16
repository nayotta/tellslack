# tellslack

Tellslack is a simple tool for sending message from github actions to slack.

To use this action, you need to set 4 environment variables:

- *SLACK_TOKEN*    a user/bot token of slack
- *SLACK_CHANNEL*  the channel you want to push messages to
- *LOG_FILE*       the file contains message to send
- *STATUS_FILE*    the file contains the exit code

When a github workflow is running, a storage volume (`/github` If I guess) which contains the repo files is passed through actions.
When you create a new file in this volume, you can access the same file in next action.

For example, if you write some logs into `/github/workspace/testing.log`, you can read these logs with the same path in next action.
And this is how *tellslack* action works.

So, if you want to send something to slack, just write your message into the file you select, and set the filename as the LOG_FILE environment variable in *tellslack*.
But you should handle the exit code of the last action yourself.
For example, if the action you use for testing returns a non-zero vaule, the testing action would fail, and the *tellslack* action would never run.
In this case you should handle the exit code of the last action, and store it into the STATUS_FILE, pass it through the actions like the logs.
The *tellslack* action will read the exit code you pass, and exit the action with this code after sending message to slack.

## Notice
Github actions and workflow are just released as beta version. Anything could be changed.
And when you use "tellslack" action, don't use `nayotta/tellslack/tell_slack@master` if you want compatibility, use `nayotta/tellslack/tell_slack@{commit_sha}` or fork it into you project as github suggests.
