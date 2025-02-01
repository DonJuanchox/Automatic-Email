from setuptools import setup, find_packages

setup(
    name="automaticemail",
    author="DonJuanchox",
    author_email="your_email@example.com",
    description="A Python module for sending and receiving emails using SMTP and IMAP.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DonJuanchox/Automatic-Email",
    packages=find_packages(),  # Finds Email.py and Email_access.py as modules
    install_requires=[
        "requests",  # Required for API interactions (if OAuth is used)
        "msal",  # Required for Microsoft OAuth authentication
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Email",
    ],
    python_requires=">=3.7",
)