import setuptools

setuptools.setup(
    name='myqr',
    version='0.2.5dev',
    packages=['MyQR','MyQR.mylibs'],
    license='MIT',
    author='Sam Korn',
    author_email='korn94sam@gmail.com',
    install_requires=[
	'pillow',
        'numpy',
        'imageio'
    ],
#    long_description=open('README.txt').read(),
	url='https://github.com/sako0938/qrcode'
)
