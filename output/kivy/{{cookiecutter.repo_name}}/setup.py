import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='{{cookiecutter.repo_name}}',
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description='{{cookiecutter.short_description}}',
    long_description=read('README.md'),
    license='MIT',
    keywords=(
        "Python, cookiecutter, kivy, buildozer, pytest, projects, project "
        "templates, example, documentation, tutorial, setup.py, package, "
        "android, touch, mobile, NUI"
    ),
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}',
    install_requires=[
        'kivy>={{cookiecutter.kivy_version}}',
    ],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: User Interfaces',
    ],
)
