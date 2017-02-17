try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'A meal planning app in line with the 4 Hour Chef diet plan',
        'author': 'Sylwia Bridges',
        'url': 'https://github.com/pumpkincouture/4-hour-recipe',
        'name': '4-hour-recipe',
        'version': '0.1',
        'install_requires': ['nose']
        }

setup(**config)
