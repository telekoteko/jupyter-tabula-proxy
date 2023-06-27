import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-tabula-proxy",
    version="1.0.0",
    url="https://github.com/telekoteko/jupyter-tabula-proxy",
    author="telekoteko",
    description="tabula",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["jupyter", "tabula", "jupyterhub", "jupyter-server-proxy"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        "jupyter-server-proxy>=1.5.0",
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "tabula = jupyter_tabula_proxy:setup_tabula",
        ]
    },
    package_data={
        "jupyter_tabula_proxy": ["icons/tabula.svg"],
    },
)