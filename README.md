# Image-Classifier-Backend

A backend for text/non-text image crawler &amp; classifier service. Part of software course project.

Root repo: https://github.com/KSkun/Image-Text-Nontext-Classifier-Service

## Features

### HTTP Application Backend

The backend is developed based on Flask framework, with RESTful API and MVC model.

API usages: see [API document](doc/api.md).

Database structure: see [database document](doc/db.md).

### Communication

The backend uses [redis stream](https://redis.io/topics/streams-intro) to send spider and classifier commands. At each
startup, it will recreate command stream and initialize consumer group for spiders and classifiers.

Command pattern: see [spider repo](https://github.com/KSkun/Image-Spider)
and [classifier repo](https://github.com/KSkun/Image-Text-Nontext-Classifier).

The image file should be stored at `./workdir/tmp/<task ObjectId>/<image filename>`. Classified images should be copied
to directory `./workdir/text/<task ObjectId>` or `./workdir/nontext/<task ObjectId>`.

### Tests

Tests are at `./test`. Includes test HTTP requests for APIs.

## Configuration

### Local Startup

An example of working environment is in `./workdir`.

Config files store in `./workdir/config`, an example can be found as `default.json`.

Configuration steps:

1. Run `pip install -r requirements.txt`.
2. Set environment variable `CONFIG_FILE` to your config filename, if not set, it's `default.json`.
3. Create symlinks from image tmp, text, non-text directory to `./workdir`
4. Inside your config file, make sure the requirements below:
    1. `host`, `port` set to backend's host & port.
    2. `image_tmp_dir`, `image_text_dir` and `image_nontext_dir` set to your symlinks as step 3.
    3. `image_url` is your static resource site prefix.
    4. `mongo_xxx` is your global MongoDB settings.
    5. `redis_xxx` is your global Redis settings.
    6. Change `jwt_secret` to a complex string, adjust token expire duration by `jwt_expire` (in minute).
5. Run `python ../src/app.py` with working directory `./workdir`.

### Docker

See [docker configuration repo](https://github.com/KSkun/Image-Text-Nontext-Classifier-Service).