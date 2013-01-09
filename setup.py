from setuptools import setup


setup(
    name='mezzanine-slides',
    version='1.0.2',
    license='Simplified BSD',

    install_requires = [
        'Mezzanine',
    ],

    description='Easily plug a slideshow into your mezzanine website on all pages.',
    long_description=open('README.md').read(),

    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',

    url='http://github.com/overshard/mezzanine-slides',
    download_url='http://github.com/overshard/mezzanine-slides/downloads',

    include_package_data=True,

    packages=['mezzanine_slides'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
