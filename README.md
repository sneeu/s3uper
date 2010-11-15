# s3uper

A simple script for uploading files via the command line to Amazon S3.


## Examples

Backup a database:

    pg_dump blog | python s3uper.py -f blog.sql

Backup a database, and timestamp the filename:

    pg_dump blog | python s3uper.py -f blog.sql -t
