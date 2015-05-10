from setuptools import setup, find_packages

setup(
    name='django-foundation-filefield-widget',
    version=__import__('foundation_filefield_widget').__version__,
    description=__import__('foundation_filefield_widget').__doc__,
    long_description=open('README.rst').read(),
    author='Philip Garnero',
    author_email='philip.garnero@gmail.com',
    url='https://github.com/PhilipGarnero/django-foundation-filefield-widget',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=False,
)
