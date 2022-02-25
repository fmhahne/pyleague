import setuptools

setuptools.setup(
    name="pyleague",
    version="0.1.0",
    author="Fernando Miguel Hahne",
    author_email="fernandomhahne@gmail.com",
    install_requires=["python-frontmatter", "typer", "rich"],
    entry_points={
        "console_scripts": ["pyleague = pyleague.__main__:main"],
    },
)
