from distutils.core import setup

setup(
    name="python-turbovote",
    version="0.0.1",
    author="Fight for the Future",
    author_email="",
    packages="turbovote",
    license="LICENSE.txt",
    description="Python wrapper for the TurboVote API",
    long_description=open("README.txt").read(),
    install_requires=[
        "requests >= 0.10.4"],
)
