# .vdata file extension decyption tool

.vdata is filetype associated with Vaulty app for Android. Vaulty can store images and videos, and this srcipt successfully decrypts them.

This repo is inspired by this gist: https://gist.github.com/lokkju/533b9c0a0783287d9168

The script I've implemented is for python 3, and supports all photo and video file types (I tested it for .mp4 and .jpg).
I use filetype package which gives correct extension based on data in files. filetype package: https://pypi.org/project/filetype/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

To install dependencies, execute this:

```
pip install -r requirements.txt
```

### Execution

The script expects two parameters, source and destination directory, and can be executed like this:

```
python vdata_decrypt_tool.py '/path/to/source/dir' '/path/to/destination/dir'
```
