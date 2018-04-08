from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Flask Session Bundle',
    version='0.1.0',
    description='Adds server-side sessions support to Flask Unchained',
    long_description=long_description,
    url='https://github.com/briancappello/flask-session-bundle',
    author='Brian Cappello',
    license='MIT',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'flask-session>=0.3.1',
        'flask-unchained>=0.2.0',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
)
