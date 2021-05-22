from setuptools import setup
import sys

if sys.version_info[0] < 3:
    with open('README.md') as f:
        long_description = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

project_urls = {'Homepage' : 'https://github.com/cptcroissant/logregnumpy'}

setup(name='logregnumpy',
      version='0.1.2',
      description='Logistic Regression Classifier',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['logregnumpy'],
      project_urls=project_urls,
      author_email='kir.klyukvin@gmail.com',
      zip_safe=False)
