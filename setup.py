from setuptools import setup
from src import __author__, __email__, __version__, __license__


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='Poloniex',
    version=__version__,
    description='(Unofficial) Poloniex.com TradeBook',
    # long_description=readme(),
    author=__author__,
    author_email=__email__,
    url='https://github.com/a904guy/poloniex-tradebook-python3',
    license=__license__,
    packages=['Poloniex'],
    package_dir={'Poloniex': 'src'},
    install_requires=[]
)
