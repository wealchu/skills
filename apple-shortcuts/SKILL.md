---
name: apple-shortcuts
description: Create and trigger Apple Shortcuts for iOS/macOS automation and cross-platform workflows
version: 1.0.0
author: ChatGPT Office Skills
category: automation
tags:
  - apple
  - shortcuts
  - ios
  - macos
  - automation
department: operations
models:
  - gpt-6-astra
mcp:
  server: apple-mcp
  tools:
    - shortcuts_run
    - shortcuts_list
    - reminders_create
    - notes_create
capabilities:
  - Shortcut execution
  - Reminders management
  - Notes creation
  - Calendar integration
input:
  - Shortcut names
  - Input parameters
  - Reminder details
  - Note content
output:
  - Shortcut results
  - Created items
  - Sync status
languages:
  - en
related_skills:
  - home-assistant
  - calendar-automation
  - obsidian-automation
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Apple Shortcuts Integration

Integrate with Apple ecosystem for iOS and macOS automation.

## Core Capabilities

### Run Shortcuts
```yaml
shortcut_execution:
  run:
    name: "Morning Routine"
    input: optional
    
  run_with_input:
    name: "Process Text"
    input: "{{text_to_process}}"
    
  run_with_clipboard:
    name: "Share to App"
    input: clipboard
```

### Apple Reminders
```yaml
reminders:
  create:
    title: "{{task}}"
    list: "Work"
    due_date: "{{date}}"
    due_time: "09:00"
    priority: high
    notes: "{{details}}"
    
  query:
    list: "Shopping"
    completed: false
    
  complete:
    reminder_id: "{{id}}"
```

### Apple Notes
```yaml
notes:
  create:
    title: "Meeting Notes - {{date}}"
    folder: "Work"
    body: |
      # {{meeting_title}}
      
      ## Attendees
      {{attendees}}
      
      ## Notes
      {{notes}}
      
  append:
    note_title: "Running Log"
    content: "- {{date}}: {{entry}}"
    
  search:
    query: "project alpha"
    folder: "Projects"
```

### Calendar
```yaml
calendar:
  create_event:
    title: "{{event_title}}"
    calendar: "Work"
    start: "{{start_time}}"
    end: "{{end_time}}"
    location: "{{location}}"
    notes: "{{notes}}"
    alerts:
      - 30  # minutes before
      
  query:
    calendar: "all"
    start: today
    end: "+7 days"
```

## Shortcut Examples

### Daily Log
```yaml
shortcut_daily_log:
  steps:
    - get_current_date
    - prompt_for_input:
        message: "How was your day?"
    - append_to_note:
        title: "Daily Journal"
        content: |
          ## {{date}}
          {{input}}
    - create_reminder:
        title: "Journal entry"
        due: tomorrow 9am
```

### Quick Capture
```yaml
shortcut_quick_capture:
  trigger: share_sheet
  steps:
    - get_shared_input
    - create_note:
        title: "Captured - {{date}}"
        body: "{{input}}"
    - notify: "Captured successfully"
```

## Integration Workflows

### Cross-Platform Sync
```yaml
sync_workflow:
  trigger: note_created
  actions:
    - if: tag == "work"
      then:
        - sync_to: notion
        - sync_to: obsidian
    - if: has_task
      then:
        - create_reminder: from_task
```

## Best Practices

1. **Naming**: Clear, descriptive shortcut names
2. **Input Handling**: Validate inputs
3. **Error Handling**: Graceful failures
4. **Privacy**: Minimize data exposure
5. **Testing**: Test on all devices
