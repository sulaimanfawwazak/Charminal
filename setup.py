from setuptools import setup

with open("README.md", 'r') as fh:
  long_description = fh.read()

setup(
  name='charminal',
  version='1.0.0',
  description='A library containing commonly used emojis for terminal messages',
  long_description=long_description,
  long_description_content_type='text/markdown',
  py_modules=['charminal'],
  author='pwnwas',
  author_email='sulaimanfawwazak@gmail.com',
  url='https://github.com/sulaimanfawwazak/pwnwas_emoji',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
)