#!/usr/bin/env python3

from setuptools import setup
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('linkbot_serialid_tool/linkbot_serialid_tool.py').read(),
    re.M
    ).group(1)

setup(
    name = "linkbot_serialid_tool",
    packages = ["linkbot_serialid_tool", ],
    version = version,
    entry_points = {
        "console_scripts": ['linkbot-serialid-tool=linkbot_serialid_tool.linkbot_serialid_tool:main']
    },
    install_requires = ["PyLinkbot >= 2.3.4"],
    description = "Tool for programming Linkbot serial IDs",
    zip_safe = False,
    include_package_data = True,
    author = "David Ko",
    author_email = "david@barobo.com",
    )

