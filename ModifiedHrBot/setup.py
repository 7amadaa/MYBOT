from setuptools import setup, find_packages

setup(
    name='highrise-bot-sdk',  # Ensure this matches what you're trying to import
    version='24.1.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'httpx',
        'attrs',
        'click',
        'quattro',
        'pendulum',
        'cattrs',
        # Add other dependencies as needed
    ],
)