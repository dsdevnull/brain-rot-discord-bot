from setuptools import setup

setup(
    name='brain-rot-discord-bot', # The name of your project
    version='0.1.0', # The version of your project
    install_requires=[
        'discord.py==2.3.2',
        'python-dotenv==1.0.1',
        'pytube==15.0.0'
    ]
)