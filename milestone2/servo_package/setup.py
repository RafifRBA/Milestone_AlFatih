from setuptools import setup

setup(
    name="servo_package",
    version="0.0.0",
    packages=["servo_pack"],

    entry_points={
        "console_scripts": [
            "servo_node = servo_pack.main:main",
        ],
    },
)