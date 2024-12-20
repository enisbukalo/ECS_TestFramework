from setuptools import setup, find_packages

setup(
    name="ecs-testframework",
    version="0.1.0",
    packages=find_packages(include=["Core", "Core.*"]),
    install_requires=[],
    python_requires=">=3.11",
)
