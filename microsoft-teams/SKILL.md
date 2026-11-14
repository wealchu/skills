---
name: microsoft-teams
description: Automate Microsoft Teams messaging, meetings, channels, and workflow integrations
version: 1.0.0
author: ChatGPT Office Skills
category: communication
tags:
  - teams
  - microsoft
  - collaboration
  - meetings
  - chat
department: operations
models:
  - gpt-6-astra
mcp:
  server: microsoft-mcp
  tools:
    - teams_message
    - teams_meeting
    - teams_channel
    - teams_webhook
capabilities:
  - Channel messaging
  - Meeting scheduling
  - Workflow automation
  - Adaptive cards
input:
  - Message content
  - Meeting details
  - Channel configurations
  - Webhook payloads
output:
  - Sent messages
  - Meeting links
  - Channel updates
  - Bot responses
languages:
  - en
related_skills:
  - slack-workflows
  - outlook-automation
  - calendar-automation
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Microsoft Teams Automation

Automate Microsoft Teams communication and collaboration workflows.

## Core Capabilities

### Channel Messaging
```yaml
message_types:
  simple_message:
    channel_id: "channel_xxx"
    message: "Hello, Team!"
    
  formatted_message:
    channel_id: "channel_xxx"
    content_type: "html"
    message: |
      <h1>Weekly Update</h1>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
      
  adaptive_card:
    channel_id: "channel_xxx"
    card:
      type: "AdaptiveCard"
      body:
        - type: "TextBlock"
          text: "Approval Required"
          weight: "bolder"
        - type: "Input.Text"
          id: "comment"
          placeholder: "Add comment"
      actions:
        - type: "Action.Submit"
          title: "Approve"
          data:
            action: "approve"
```

### Meeting Automation
```yaml
meeting_creation:
  subject: "Weekly Standup"
  start: "2024-01-20T09:00:00"
  end: "2024-01-20T09:30:00"
  attendees:
    - "user1@company.com"
    - "user2@company.com"
  is_online_meeting: true
  settings:
    allow_new_time_proposals: true
    lobby_bypass: "organization"
    record_automatically: false
```

### Incoming Webhooks
```yaml
webhook_message:
  url: "https://outlook.webhook.office.com/..."
  payload:
    "@type": "MessageCard"
    themeColor: "0076D7"
    summary: "Deployment Complete"
    sections:
      - activityTitle: "Production Deployment"
        activitySubtitle: "v2.1.0 deployed successfully"
        facts:
          - name: "Environment"
            value: "Production"
          - name: "Duration"
            value: "5 minutes"
        markdown: true
    potentialAction:
      - "@type": "OpenUri"
        name: "View Dashboard"
        targets:
          - os: "default"
            uri: "https://dashboard.example.com"
```

### Bot Workflows
```yaml
bot_commands:
  /status:
    description: "Check system status"
    response:
      type: adaptive_card
      template: status_card
      
  /create-ticket:
    description: "Create support ticket"
    parameters:
      - title: required
      - priority: optional
    action: create_jira_issue
    
  /approve {id}:
    description: "Approve request"
    action: process_approval
    response: "Request {{id}} approved ✓"
```

## Integration Workflows

### CI/CD Notifications
```yaml
pipeline_notifications:
  on_build_start:
    channel: "#deployments"
    card:
      title: "🚀 Build Started"
      fields:
        - Branch: "{{branch}}"
        - Triggered by: "{{user}}"
        
  on_build_complete:
    channel: "#deployments"
    card:
      title: "{{#if success}}✅{{else}}❌{{/if}} Build {{status}}"
      fields:
        - Duration: "{{duration}}"
        - Tests: "{{tests_passed}}/{{tests_total}}"
      actions:
        - title: "View Logs"
          url: "{{logs_url}}"
```

### Approval Workflows
```yaml
approval_flow:
  trigger: expense_submitted
  actions:
    - send_adaptive_card:
        channel: "#approvals"
        card:
          title: "Expense Approval"
          body: "{{employee}} submitted ${{amount}}"
          actions:
            - Approve
            - Reject
    - wait_for_response:
        timeout: 48_hours
    - process_decision:
        approved: update_expense_status
        rejected: notify_submitter
```

## Best Practices

1. **Rate Limits**: Respect Microsoft Graph limits
2. **Adaptive Cards**: Use for rich interactions
3. **Permissions**: Request minimal scopes
4. **Threading**: Reply in threads for context
5. **Mentions**: Use @mentions sparingly
6. **Webhooks**: Use for one-way notifications
