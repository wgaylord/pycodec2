from setuptools import setup, find_packages

setup(
    name='pycodec2',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/wgaylord/pycodec2',
    license='MIT',
    author='William Gaylord',
    author_email='chibill110@gmail.com',
    description='Python wrapper for the codec2 library'
)
