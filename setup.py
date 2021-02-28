import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()
    
setuptools.setup(
    name='nhlclient',
    version='0.0.1',
    author='@nolanbradshaw',
    description='An API wrapper for the undocumented NHL API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nolanbradshaw/nhlclient',
    install_requires=['requests>=2.20.0',]
)