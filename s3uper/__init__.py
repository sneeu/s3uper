import datetime
import mimetypes
from optparse import OptionParser
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


def main():
    parser = OptionParser()
    parser.add_option('-f', '--filename', dest='filename',
                      help="write stdin as FILENAME", metavar="FILENAME")
    parser.add_option('-t', '--timestamp', action="store_true", dest='timestamp',
                      help="add a timestamp to the filename", default=False)

    options, args = parser.parse_args()

    filename = options.filename

    if options.timestamp:
        root, ext = os.path.splitext(filename)
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%dT%H%M%S')
        filename = '%s.%s%s' % (root, timestamp, ext)
    upload_s3(filename)


if __name__ == "__main__":
    main()
