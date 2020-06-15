import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='smtpgmail-Python3.8',  # Replace with your own username
    version='0.0.1',
    author='Pranav Balaji Pooruli',
    author_email='pranav.pooruli@gmail.com',
    description='A small package that lets you send Gmail messages from Python script for free!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Python3-8/smtpgmail',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
