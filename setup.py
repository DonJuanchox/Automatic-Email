from setuptools import setup, find_packages

setup(
    name="EmailAutomation",
    version="1.0.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A Python module for sending and receiving emails using SMTP and IMAP.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/EmailAutomation",
    packages=find_packages(),  # Automatically discovers packages
    install_requires=[  # No external dependencies required
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Email",
    ],
    python_requires=">=3.7",
)