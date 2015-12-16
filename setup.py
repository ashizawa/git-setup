from setuptools import setup, find_packages

setup(
    name='git-setup',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts':
            'git-setup = git_setup:setup'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
    ],
)
