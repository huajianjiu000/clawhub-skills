---
name: sql-query-optimizer
description: AI-powered SQL query optimization assistant. Analyzes slow queries, identifies performance bottlenecks, suggests index strategies, and rewrites queries for better performance. Use when debugging slow database operations or optimizing query performance.
version: 1.0.0
author: muqing
tags: [database, sql, performance, optimization]
---

# SQL Query Optimizer

## Description

An AI-powered SQL query optimization assistant that analyzes slow queries, identifies performance bottlenecks, suggests index strategies, and rewrites queries for optimal performance. Helps databases run faster and more efficiently.

## When to Use

- Optimizing slow-running queries
- Debugging database performance issues
- Designing efficient indexes
- Analyzing query execution plans
- Reducing database load
- Improving application responsiveness

## Optimization Techniques

### 1. Index Optimization
- Identify missing indexes
- Analyze index selectivity
- Consider composite indexes
- Review index usage
- Remove unused indexes

### 2. Query Rewrite
- Eliminate subqueries where JOINs work better
- Use EXISTS instead of IN for large sets
- Avoid SELECT *
- Use appropriate JOIN types
- Filter early with WHERE clauses
- Use LIMIT for pagination

### 3. Schema Optimization
- Normalize for writes
- Denormalize for reads
- Partition large tables
- Archive old data
- Choose appropriate data types

### 4. Execution Plan Analysis
- Full table scans → Index seeks
- Nested loops → Hash joins
- High row counts → Better filters

## Common Patterns

### Slow Pattern: N+1 Queries
```sql
-- Bad: N+1 queries
SELECT * FROM orders;
-- Then for each order:
SELECT * FROM customers WHERE id = ?;

-- Good: Single JOIN query
SELECT o.*, c.* FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

### Slow Pattern: Functions on Columns
```sql
-- Bad: Function disables index
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- Good: Range query uses index
SELECT * FROM users 
WHERE created_at >= '2024-01-01' 
AND created_at < '2025-01-01';
```

### Slow Pattern: OR Conditions
```sql
-- Bad: Full table scan
SELECT * FROM products WHERE price > 100 OR stock < 10;

-- Good: UNION of indexed queries
SELECT * FROM products WHERE price > 100
UNION ALL
SELECT * FROM products WHERE price <= 100 AND stock < 10;
```

## Output Format

```markdown
## Query Optimization Report

### Original Query
```sql
[Original slow query]
```

### Issues Identified
1. [Issue 1] - Impact: [High/Medium/Low]
2. [Issue 2] - Impact: [High/Medium/Low]

### Optimized Query
```sql
[Rewritten efficient query]
```

### Recommended Indexes
```sql
CREATE INDEX idx_name ON table(column);
```

### Expected Improvement
- Execution time: [X]% faster
- Rows scanned: [X]% reduction

### Before/After Comparison
| Metric | Before | After |
|--------|--------|-------|
| Execution Time | 500ms | 50ms |
| Rows Scanned | 100000 | 1000 |
| Index Used | No | Yes |
```

## Example

**Input**: "Optimize this query that takes 5 seconds"

**Analysis**:
1. Review query structure
2. Check execution plan
3. Identify missing indexes
4. Rewrite problematic patterns

**Output**: Optimized query with explanation and expected improvements
```
