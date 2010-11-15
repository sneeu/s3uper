from distutils.core import setup


setup(
    name = "s3uper",
    packages = ["s3uper"],
    version = "0.1.0",
    description = "Simple S3 uploader",
    author = "John Sutherland",
    author_email = "john@sneeu.com",
    keywords = ["amazon", "s3", "upload", "backup"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: System :: Archiving :: Backup",
    ]
)