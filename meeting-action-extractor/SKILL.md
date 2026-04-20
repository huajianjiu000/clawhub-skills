---
name: meeting-action-extractor
description: AI-powered meeting notes analyzer that extracts action items, decisions, deadlines, and key takeaways from meeting transcripts or notes. Automatically assigns owners and priorities. Use when processing meeting notes, tracking commitments, or managing action items.
version: 1.0.0
author: muqing
tags: [productivity, meetings, task-management, notes]
---

# Meeting Action Extractor

## Description

An AI-powered meeting notes analyzer that extracts action items, decisions made, deadlines, and key takeaways from meeting transcripts or notes. Automatically assigns owners and priorities to track commitments effectively.

## When to Use

- Processing meeting transcripts
- Extracting action items from notes
- Tracking team commitments
- Following up on decisions
- Creating meeting summaries
- Managing project tasks

## Extraction Categories

### 1. Action Items
- Task description
- Owner (person responsible)
- Due date/deadline
- Priority (High/Medium/Low)
- Status (Open/Complete)
- Dependencies

### 2. Decisions Made
- Decision description
- Rationale
- Stakeholders involved
- Date decided
- Related decisions

### 3. Key Discussion Points
- Topics covered
- Important insights
- Points of contention
- Consensus reached

### 4. Important Dates
- Upcoming deadlines
- Scheduled meetings
- Milestones
- Project timelines

### 5. Risks & Blockers
- Identified risks
- Current blockers
- Mitigation plans

## Output Format

```markdown
## Meeting Summary: [Title]

**Date:** [Date]
**Attendees:** [Names]
**Duration:** [Length]

---

### Action Items

| # | Action | Owner | Due | Priority | Status |
|---|--------|-------|-----|----------|--------|
| 1 | [Task] | [Name] | [Date] | 🔴 High | ⏳ Open |
| 2 | [Task] | [Name] | [Date] | 🟡 Med | ⏳ Open |

---

### Decisions Made

1. **Decision:** [What was decided]
   - Rationale: [Why]
   - Date: [When]
   
2. **Decision:** [Next decision]

---

### Key Takeaways

- [Important point 1]
- [Important point 2]
- [Important point 3]

---

### Risks & Blockers

⚠️ **Risk:** [Description]
   **Mitigation:** [Plan]

🚧 **Blocker:** [Description]
   **Owner:** [Name]

---

### Follow-up Meeting
- **Date:** [Next meeting]
- **Agenda:** [Topics to cover]
```

## Extraction Rules

### Owner Assignment
- Look for names mentioned with action verbs
- Default to meeting organizer if unclear
- Use "Team" for shared responsibilities

### Priority Guidelines
- **High**: External deadlines, blocking issues
- **Medium**: Important but not urgent
- **Low**: Nice-to-have improvements

### Date Extraction
- Explicit dates ("by March 15")
- Relative dates ("next week", "ASAP")
- Meeting cadence ("weekly", "monthly")

## Example

**Input**: Meeting transcript with multiple speakers discussing project timeline

**Output**:
- 5 action items with owners
- 3 key decisions
- 2 deadlines
- 1 blocker identified
- Structured summary

## Integration Tips

1. Copy extracted items to project management tools
2. Send to task assignee for confirmation
3. Add to calendar for deadline reminders
4. Share summary with all attendees
```
