from distutils.core import setup

"""
clibobo
------
Gets Latest News, Gist and more from your favourite Nigerian Sites
To your terminal 

"""


setup(
  name = 'clibobo',
  version = '0.1',
  packages = ['clibobo'],
  description = 'Gets Latest News,Gist and more from your favourite Sites comfortably in your terminal',
  author = 'Obi Uchenna David',
  author_email = 'daviduchenna@outlook.com',
  url = 'https://github.com/othreecodes/clibobo', 
  download_url = 'https://github.com/othreecodes/clibobo/tarball/0.1', 
  keywords = ['news','gist','stories','information'],
  entry_points="""
             [console_scripts]
             clibobo = clibobo.clibobo:main
        """,
  install_requires=[
	'requests',
	'feedparser',
	'colorama'	
  ],
  classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
