from setuptools import setup

setup(
    name="nxbt",
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=[
        "dbus-python",
        "Flask",
        "Flask-SocketIO",
        "eventlet",
        "blessed",
        "pynput",
        "psutil",
        "cryptography",
        "jinja2",
        "itsdangerous",
        "Werkzeug",
    ],
    extra_require={
        "dev": [
            "pytest"
        ]
    }
)
