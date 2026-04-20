---
name: bug-fixer
description: AI-powered bug diagnosis and fixing assistant. Analyzes error messages, traces bugs to root causes, and provides detailed fix suggestions with code examples. Use when debugging code, fixing runtime errors, or troubleshooting unexpected behavior.
version: 1.0.0
author: muqing
tags: [development, debugging, bug-fix, troubleshooting]
---

# Bug Fixer

## Description

An AI-powered bug diagnosis and fixing assistant that analyzes error messages, traces bugs to their root causes, and provides detailed fix suggestions with code examples. Helps developers quickly identify and resolve software defects.

## When to Use

- Debugging runtime errors
- Fixing unexpected behavior
- Troubleshooting error messages
- Investigating crash reports
- Analyzing stack traces
- Solving logical bugs

## Diagnosis Framework

### Step 1: Understand the Error
- Error type and message
- Error location (file, function, line)
- Stack trace analysis
- When the error occurs

### Step 2: Gather Context
- Recent code changes
- Environment conditions
- Input data that triggers the bug
- Expected vs actual behavior

### Step 3: Root Cause Analysis
- Is this a syntax error?
- Is this a runtime exception?
- Is this a logical error?
- Is this a concurrency issue?
- Is this an environmental issue?

### Step 4: Generate Fix
- Immediate fix
- Long-term solution
- Prevention measures

## Common Bug Patterns

### Null/Undefined Errors
```
Problem: Cannot read property 'x' of undefined
Solution: Add null checks, optional chaining
```

### Async/Await Issues
```
Problem: Promise not handled, race conditions
Solution: Proper await handling, Promise.all for parallel
```

### Type Errors
```
Problem: Type 'string' is not assignable to type 'number'
Solution: Type conversion, type guards
```

### Memory Leaks
```
Problem: Objects not garbage collected
Solution: Proper cleanup, remove event listeners
```

## Output Format

```
## Bug Analysis Report

### Error Information
- Type: [Error type]
- Location: [File:Line:Function]
- Message: [Error message]

### Root Cause
[Detailed explanation of why the bug occurs]

### Immediate Fix
```[language]
[Fixed code]
```

### Long-term Solution
[How to prevent this bug in the future]

### Test Case
```[language]
[Unit test to verify the fix]
```

### Related Issues
- [Similar bugs to check]
```

## Example

**Input**: "Fix this TypeError: Cannot read property 'map' of undefined"

**Analysis**:
1. Identify where map() is called
2. Trace what variable is undefined
3. Find why it's undefined
4. Provide fix with null check

**Output**: Detailed analysis with code fix and test case
