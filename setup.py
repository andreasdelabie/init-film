import setuptools

install_requires = []

setuptools.setup(
    name="init-film",
    version="0.2.2a",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'init-film = main:__main__',
        ],
    },
    include_package_data=True,
    )