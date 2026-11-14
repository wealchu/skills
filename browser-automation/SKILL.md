---
name: browser-automation
description: Automate web browser interactions, scraping, testing, and workflow automation with Puppeteer/Playwright
version: 1.0.0
author: ChatGPT Office Skills
category: automation
tags:
  - browser
  - puppeteer
  - playwright
  - scraping
  - testing
department: engineering
models:
  - gpt-6-astra
mcp:
  server: browser-mcp
  tools:
    - browser_navigate
    - browser_click
    - browser_type
    - browser_screenshot
capabilities:
  - Page navigation
  - Element interaction
  - Data extraction
  - Screenshot capture
input:
  - URLs
  - Selectors
  - Actions
  - Scripts
output:
  - Extracted data
  - Screenshots
  - Test results
  - Automation logs
languages:
  - en
related_skills:
  - web-search
  - deep-research
  - etl-pipeline
---

## Model and execution requirement

Use OpenAI GPT-6 Astra (`gpt-6-astra`), the highest-capability general model verified for this release. Use the strongest supported reasoning setting in the actual host; the API reference configuration uses `max`. Do not route through another model provider or silently downgrade. If this model is unavailable, report that blocker before model-dependent execution. A skill cannot switch the host model: verify the actual session selection separately. Follow the user's current account rules and task permissions. Consult the repository's `MODEL_POLICY.md` for the verified release date, official sources, and update procedure.

# Browser Automation

Automate web browser interactions for scraping, testing, and workflow automation.

## Core Capabilities

### Navigation
```yaml
navigation:
  goto:
    url: "https://example.com"
    wait_until: "networkidle"
    timeout: 30000
    
  actions:
    - wait_for_selector: ".content"
    - scroll_to_bottom: true
    - wait_for_navigation: true
```

### Element Interaction
```yaml
interactions:
  click:
    selector: "button.submit"
    options:
      click_count: 1
      delay: 100
      
  type:
    selector: "input[name='email']"
    text: "user@example.com"
    options:
      delay: 50  # Human-like typing
      
  select:
    selector: "select#country"
    value: "US"
    
  file_upload:
    selector: "input[type='file']"
    files: ["document.pdf"]
```

### Data Extraction
```yaml
scraping:
  extract_text:
    selector: ".article-content"
    
  extract_all:
    selector: ".product-card"
    fields:
      name: ".product-name"
      price: ".price"
      url:
        selector: "a"
        attribute: "href"
        
  extract_table:
    selector: "table.data"
    output: json
```

### Screenshots & PDF
```yaml
capture:
  screenshot:
    path: "screenshot.png"
    full_page: true
    type: "png"
    
  pdf:
    path: "page.pdf"
    format: "A4"
    print_background: true
```

## Workflow Examples

### Form Automation
```javascript
// Login and fill form
await page.goto('https://app.example.com/login');
await page.fill('#email', 'user@example.com');
await page.fill('#password', 'securepass');
await page.click('button[type="submit"]');
await page.waitForNavigation();

// Navigate to form
await page.click('a[href="/new-entry"]');
await page.fill('#title', 'Automated Entry');
await page.fill('#description', 'Created via automation');
await page.click('button.submit');
```

### Web Scraping
```yaml
scraping_workflow:
  - navigate: "https://news.example.com"
  - wait: ".article-list"
  - extract_all:
      selector: ".article"
      fields:
        title: "h2"
        summary: ".excerpt"
        link:
          selector: "a"
          attribute: "href"
  - paginate:
      next_button: ".pagination .next"
      max_pages: 10
  - output: "articles.json"
```

### E2E Testing
```yaml
test_workflow:
  - name: "User Registration"
    steps:
      - goto: "/register"
      - fill:
          "#email": "test@example.com"
          "#password": "Test123!"
      - click: "button[type='submit']"
      - assert:
          selector: ".success-message"
          text_contains: "Welcome"
```

## Best Practices

1. **Wait Strategies**: Use proper waits
2. **Error Handling**: Catch navigation failures
3. **Rate Limiting**: Be respectful to servers
4. **Headless Mode**: Use for production
5. **Selectors**: Prefer data-testid attributes
6. **Screenshots**: Capture on failures
