FROM debian:9.5-slim

LABEL "com.github.actions.name"="Send message to slack"
LABEL "com.github.actions.description"="Read log from file left by the last action, and send it to slack with given account"
LABEL "com.github.actions.icon"="mic"
LABEL "com.github.actions.color"="purple"

LABEL "repository"="http://github.com/bingliu221/actions"
LABEL "maintainer"="Bing Liu <bingliu221@gmail.com>"

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
