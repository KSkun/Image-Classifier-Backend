# Image-Classifier-Backend API Doc

## Data Exchange Format

All `GET` requests pass data via URL parameters, `POST` requests via request body with content type `application/json`.

Response is always a JSON document like below:

```json
{
  "success": true,
  "error": "if success is false, here's error message",
  "data": {}
}
```

Response data is always in `data` field.

Authorization via JWT token in `Authorization` header in `Bearer` schema, like:

```
Authorization: Bearer token_content
```

If API needs authorization, a mark `(auth)` will present at the first line of description.

## /api/user

### GET /api/user/token

Check if username and password matches, then sign a token for authorization.

Request: URL parameters

- `username`: username
- `password`: base64-encoded password

Response:

```json
{
  "token": "JWT token",
  "expire_at": 1642018994.149235
}
```

## /api/task

### GET /api/task/engines

Get available search engine list.

Request: (empty)

Response:

```json
{
  "engines": [
    {
      "display_name": "百度",
      "name": "baidu"
    },
    {
      "display_name": "Google",
      "name": "google"
    }
  ]
}
```

### POST /api/task

(auth) Create new task.

Request:

```json
{
  "keyword": "keyword",
  "engines": [
    "baidu"
  ],
  "limit": 10
}
```

Response:

```json
{
  "_id": "task ObjectId"
}
```

### GET /api/task/list

(auth) Get task list created by current user.

Request: (empty)

Response:

```json
{
  "tasks": [
    {
      "classifier_done": true,
      "engines": [
        "baidu"
      ],
      "id": "task ObjectId",
      "keyword": "keyword",
      "limit": 10,
      "spider_done": true
    }
  ]
}
```

### GET /api/task/\<task_id\>

(auth) Get detailed info of the task.

Request: URL variable

- `<task_id>`: task ObjectId

Response:

```json
{
  "classifier_done": true,
  "engines": [
    "baidu"
  ],
  "keyword": "keyword",
  "limit": 10,
  "spider_done": true
}
```

### GET /api/task/\<task_id\>/zip/\<class\>

(auth) Get zipped image pack of specified class of the task.

Request: URL variable

- `<task_id>`: task ObjectId
- `<class>`: image class, one of `text`, `nontext`

Response:

```json
{
  "file": "zipped file url"
}
```

## /api/image

### GET /api/image/list

(auth) Get image list of specified task.

Request: URL parameter

- `task`: task ObjectId

Response:

```json
{
  "images": [
    {
      "class": "text",
      "url": "image file url"
    }
  ]
}
```