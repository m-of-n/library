#!/bin/bash
input=$(cat)
prompt=$(jq -r '.prompt // empty' <<<"$input")

case "$prompt" in
  /speckit.plan*)      file="specs/threat-model.md" ;;
  /speckit.implement*) file="docs/secure-coding-rules.md" ;;
  /speckit.review*)    file="docs/security-review-checklist.md" ;;
  *) exit 0 ;;
esac

jq -nc --arg ctx "$(cat "$file")" \
  '{hookSpecificOutput: {hookEventName: "UserPromptSubmit",
    additionalContext: $ctx}}'
