import io
import os
from setuptools import setup


os.chdir(os.path.abspath(os.path.dirname(__file__)))

setup(name='unicode',
      version='2.6',
      scripts=['unicode', 'paracode'],
#      entry_points={'console_scripts': [
#          'unicode = unicode:main',
#          'paracode = paracode:main']},
      description="Display unicode character properties",
      author="Radovan Garabik",
      author_email='radovan.garabik@kassiopeia.juls.savba.sk',
      url='http://kassiopeia.juls.savba.sk/~garabik/software/unicode.html',
      license='GNU GPL v3',
      keywords=['unicode', 'character properties', 'encoding'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Text Editors :: Text Processing',
          'Topic :: Utilities'])

