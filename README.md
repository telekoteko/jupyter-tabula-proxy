# jupyter-pgweb-proxy

This package was built from the [`illumidesk/cookiecutter-jupyter-server-proxy`](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy) template.

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

## Quick Starts

### Run locally with `docker-compose`

```bash
make dev
```

### Cleanup

Stop services:

```bash
make dev-down
```

Remove images and running containers:

> **NOTE**: this will stop all running containers on the local, including those with the exit status.

```bash
make clean-all
```
