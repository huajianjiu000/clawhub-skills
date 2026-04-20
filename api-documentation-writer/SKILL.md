---
name: api-documentation-writer
description: AI-powered API documentation generator that creates comprehensive, developer-friendly API docs including endpoints, parameters, request/response examples, error codes, and authentication details. Use when documenting APIs, creating SDKs, or generating developer guides.
version: 1.0.0
author: muqing
tags: [development, documentation, api, developer-tools]
---

# API Documentation Writer

## Description

An AI-powered API documentation generator that creates comprehensive, developer-friendly API documentation including endpoints, parameters, request/response examples, error codes, and authentication details. Generates documentation that developers love to use.

## When to Use

- Writing API documentation from scratch
- Updating existing API docs
- Creating SDK documentation
- Writing developer guides
- Documenting REST APIs
- Describing GraphQL schemas
- Explaining webhook payloads

## Documentation Components

### 1. Overview Section
- API purpose and capabilities
- Base URL and version
- Authentication methods
- Rate limits
- Common headers

### 2. Endpoint Documentation
For each endpoint:
- HTTP method and path
- Description
- Authentication required
- Path parameters
- Query parameters
- Request body schema
- Request example
- Success response
- Error responses
- Code samples

### 3. Data Models
- Object schemas
- Field types and formats
- Enums and valid values
- Relationships between models

### 4. Authentication
- API key format
- OAuth flows
- Token refresh
- Permission scopes

## Output Format

```markdown
# API Documentation

## Overview
[API description]

## Authentication
[Auth instructions]

## Endpoints

### GET /resource
Description of the endpoint

**Parameters**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | Resource ID |

**Request Example**
```json
{
  "example": "value"
}
```

**Response 200**
```json
{
  "data": "result"
}
```

**Error Codes**
| Code | Description |
|------|-------------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |
```

## OpenAPI Integration

Generate OpenAPI 3.0 spec compatible output:

```yaml
openapi: 3.0.0
info:
  title: API Name
  version: 1.0.0
paths:
  /endpoint:
    get:
      summary: Endpoint description
      responses:
        '200':
          description: Success
```

## Best Practices

1. Use clear, consistent naming
2. Include realistic examples
3. Document all error cases
4. Specify field constraints
5. Add deprecation notices
6. Include changelog

## Example

**Input**: "Document a user management API with CRUD operations"

**Output**: Complete API documentation with:
- Authentication section
- User object schema
- All CRUD endpoints
- Request/response examples
- Error handling
- Code samples in multiple languages
```
