from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='spiel',
      version='0.1',
      description='Voice recognition server',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='voice recognition flask',
      url='http://github.com/Lightslayer/spiel',
      author='Liam Deacon',
      author_email='liam.m.deacon@gmail.com',
      license='MIT',
      packages=['spiel'],
      install_requires=[
          'flask',
      ],
      include_package_data=True,
      zip_safe=False)