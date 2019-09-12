from setuptools import setup

setup(name='my_hello_Giulia',
      version='0.1',
      author="GiuPassarelli",
      packages=['my_hello'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Microsoft :: Windows",
      ],
      scripts=['scripts/hello.py'],
      install_requires=[
      ],
      python_requires='>=3.6',
      )