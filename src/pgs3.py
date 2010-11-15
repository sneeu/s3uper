import mimetypes
import os.path
import sys
import S3


try:
    from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME
except ImportError:
    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
    BUCKET_NAME = 'BUCKET_NAME'


def upload_s3(filename):
    conn = S3.AWSAuthConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

    filedata = sys.stdin.read()

    content_type = mimetypes.guess_type(filename)[0]
    if not content_type:
        content_type = 'text/plain'

    headers = {'x-amz-acl': 'authenticated-read', 'Content-Type': content_type}

    response = conn.put(BUCKET_NAME, filename, S3.S3Object(filedata), headers)

    print response.message


def usage():
    print """cat somefile | python pgs3.py somefile.ext"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit()

    filename = sys.argv[1]
    upload_s3(filename)
