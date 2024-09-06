import setuptools

install_requires = []

setuptools.setup(
    name="init-film",
    version="0.2.1a",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'init-film = main',
        ],
    },
    include_package_data=True,
    )