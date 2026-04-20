---
name: task-breakdown-assistant
description: AI-powered task decomposition assistant that breaks complex projects into manageable sub-tasks, estimates effort, identifies dependencies, and creates actionable work plans. Use when planning projects, sprint planning, or managing complex work.
version: 1.0.0
author: muqing
tags: [productivity, project-management, planning, task-management]
---

# Task Breakdown Assistant

## Description

An AI-powered task decomposition assistant that breaks complex projects into manageable sub-tasks, estimates effort and duration, identifies dependencies, and creates actionable work plans. Transform overwhelming projects into clear, executable steps.

## When to Use

- Breaking down complex projects
- Sprint planning
- Estimating work effort
- Identifying task dependencies
- Creating project timelines
- Managing technical debt
- Planning feature development

## Decomposition Framework

### Step 1: Understand the Goal
- Define the end objective
- Clarify success criteria
- Identify constraints
- Set timeline

### Step 2: Identify Major Phases
- Discovery/Research
- Design/Planning
- Development/Build
- Testing/Review
- Deployment/Launch
- Maintenance/Support

### Step 3: Break Into Tasks
Each sub-task should be:
- **Specific**: Clear, unambiguous
- **Measurable**: Can verify completion
- **Achievable**: Realistic given resources
- **Relevant**: Contributes to goal
- **Time-bound**: Has estimated duration

### Step 4: Identify Dependencies
- Sequential (B depends on A)
- Parallel (C and D can run together)
- External (waits for outside input)

### Step 5: Estimate & Prioritize
- Effort (hours/days)
- Priority (Must/Should/Could)
- Owner assignment

## Task Definition Guidelines

### Good Tasks
- "Create user login form"
- "Write unit tests for auth module"
- "Design database schema"
- "Review API documentation"

### Bad Tasks (Too Vague)
- "Work on auth"
- "Test the app"
- "Improve performance"
- "Update documentation"

## Output Format

```markdown
## Task Breakdown: [Project Name]

**Total Estimated Duration:** [X days/weeks]
**Complexity:** [Low/Medium/High]

---

### Phase 1: [Name]
**Duration:** [X days]

| # | Task | Effort | Priority | Dependencies |
|---|------|--------|----------|--------------|
| 1.1 | [Task] | 2h | 🔴 High | None |
| 1.2 | [Task] | 4h | 🟡 Med | 1.1 |
| 1.3 | [Task] | 3h | 🟢 Low | 1.1, 1.2 |

---

### Phase 2: [Name]
**Duration:** [X days]

| # | Task | Effort | Priority | Dependencies |
|---|------|--------|----------|--------------|
| 2.1 | [Task] | 8h | 🔴 High | 1.3 |
| 2.2 | [Task] | 4h | 🟡 Med | 1.3 |

---

### Dependency Graph
```
[Task A] → [Task B] → [Task C]
     ↓            ↓
[Task D]    [Task E] → [Task F]
```

---

### Resource Allocation
- **Development:** 60%
- **Testing:** 20%
- **Review/Deploy:** 20%

---

### Risk Assessment
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [High] | [Plan] |
```

## Effort Estimation

### Time Ranges
- **Quick**: 1-2 hours
- **Short**: 4-8 hours (1 day)
- **Medium**: 1-2 days
- **Long**: 3-5 days
- **Extended**: 1+ weeks

### Factors to Consider
- Complexity
- Team experience
- External dependencies
- Testing requirements
- Documentation needs

## Example

**Input**: "Plan a new feature to add user notifications"

**Output**:
- 4 phases: Design, Backend, Frontend, Testing
- 15+ individual tasks
- Task dependencies mapped
- Effort estimates per task
- Total timeline calculation
```
