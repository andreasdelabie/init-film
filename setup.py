import setuptools

install_requires = []

setuptools.setup(
    name="init-film",
    version="1.0.0",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'init-film = main:main',
        ],
    },
    include_package_data=True,
    )