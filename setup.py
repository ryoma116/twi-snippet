import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="twippets",
    version="0.0.1",
    author="Ryoma Uehara",
    description="Snippet from the twitter api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryoma116/twippets",
    packages=["twippets"],
    package_dir={"twippets": "twippets"},
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    python_requires='>=3.7',
)
