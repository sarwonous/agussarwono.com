+++
categories = ["tips"]
date = "2021-03-18T09:37:36Z"
draft = false
tags = ["git","commit","jira","issue","branch"]
title = "Prepend your commit with JIRA ticket number"
description = "automaticaly prepend your commit with JIRA ticket or a branch name"

[[resources]]
name = 'step1'
src = 'images/header.png'
[[resources]]
name = 'step1'
src = 'images/1.png'
[[resources]]
name = 'step2'
src = 'images/2.png'
[[resources]]
name = 'step3'
src = 'images/3.png'

+++

#### Introduction

Tired putting your ticket number on your commit?
Use this git hook to automatically prepend your commit with a Jira ticket based on your branch name

we will use git hooks to achieve this, using the `prepare-commit-msg` hook, this will read your branch name, scan if there is a jira ticket pattern, and prepend your commit message with it

#### Step 1

Create a new `prepare-commit-msg` file or rename `prepare-commit-msg.sample` on folder `<your-repo>/.git/hooks/`
{{<figure src="images/1.png">}}

#### Step 2

Use your favorite text editor, open file prepare-commit-msh and write the following code

```bash
#!/bin/bash
FILE=$1
MESSAGE=$(cat $FILE)

TICKET=[$(git rev-parse --abbrev-ref HEAD | grep -Eo '^(\w+/)?(\w+[-_])?[0-9]+' | grep -Eo '(\w+[-])?[0-9]+' | tr "[:lower:]" "[:upper:]")]

if [[$TICKET == "[]" || "$MESSAGE" == "$TICKET"*]];then
exit 0;
fi
echo "$TICKET $MESSAGE" > $FILE
```

#### Step 3

Open your terminal and type the following command
{{<highlight bash>}}
chmod +x <yourrepo>/.git/hooks/prepare-commit-msg
{{</highlight>}}

#### Step 4

Test using git commit

{{<figure src="images/sample.png">}}
