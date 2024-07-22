from setuptools import setup, find_packages

setup(
    name="wrapper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    extras_require={
        "dev": ["pytest", "requests-mock", "poetry"],
    },
    description="A simple API wrapper package",
    author="Your Name",
    author_email="linas.kulbaciauskas@gmail.com",
    url="https://github.com/Warfere/eso-api-wrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
