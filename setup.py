from setuptools import setup

setup(name="assignment3",
      version="0.1",
      description="LED Testing for assignment3 in COMP30670",
      url="",
      author="chenzeng",
      author_email="chen.zeng@ucdconnect.ie",
      license="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['test=src.main:main']
          },
      install_requires=[
          'numpy',
                        ],
      )