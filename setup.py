from setuptools import setup, find_packages

setup(
    name='material_database',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['*.txt', '*.dat'],
    },
    url='http://gitbucket.mbi-berlin.de/steinbac/MBIMaterialDatabase',
    install_requires=['numpy',
                      'pint',
                      'pytest',
                      'tabulate',
                      'bibtexparser>=0.18.2',
                      'PyYAML>=5.1'],
    license='MIT',
    author='Felix Steinbach, Daniel Schick, et. al.',
    author_email='steinbac@mbi-berlin.de',
    description='A material database',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    keywords='material database',
)
