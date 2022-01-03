import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telegramtui",
    version="0.1.2",
    author="Valery Krasnoselsky",
    author_email="valery.krasnoselsky@gmail.com",
    description="Telegram client on your console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='telegram telegramtui telegramcli telegram-cli telegram-tui tui',
    url="https://github.com/vtr0n/TelegramTUI",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.4',
    install_requires=[
        "Pillow",
        "pyaes",
        "pyasn1",
        "PySocks",
        "python-aalib",
        "rsa",
        "Telethon",
    ],
    entry_points={
        'console_scripts': [
            'telegramtui=telegramtui.__main__:main',
            'telegram-tui=telegramtui.__main__:main',
        ]
    },
)
