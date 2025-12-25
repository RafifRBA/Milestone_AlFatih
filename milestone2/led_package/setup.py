from setuptools import setup

setup(
    name="led_package",
    version="0.0.0",
    packages=["led_package"],

    entry_points={
        "console_scripts": [
            "hello_node = led_package.main:main",
        ],
    },
)