# Image-Classifier-Backend Database Structure Doc

## MongoDB

### User document

Collection: `user`

- `_id`: ObjectId, user ID
- `username`: String, username
- `password`: String, bcrypt-hashed password

### Task document

Collection: `task`

- `_id`: ObjectId, task ID
- `keyword`: String, keyword
- `engines`: Array\<String\>, list of engines to crawl
- `limit`: Integer, result count limit
- `user`: ObjectId, owner user ID
- `spider_done`: Boolean, if spider command was done
- `classifier_done`: Boolean, if classify command was done

### Image document

Collection: `image`

- `_id`: ObjectId, image ID
- `class`: String, image class, one of `text`, `nontext`
- `task_id`: ObjectId, image related task ID
- `url`: String, image file URL

## Redis

- `spider_cmd`: stream
- `classify_cmd`: stream
