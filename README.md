# Python code on random things

Generally, this repository is somewhat of a dumping ground of code I find useful. All of it is focused on Python.

Feel free to take what you'd like!

# Docker + Jupyter

I am quite fond of [Docker](https://www.docker.com/) and Platforms as a Service in general (PaaS), I use Docker and [Jupyter](https://jupyter.org/index.html) to get up and running quickly on local environments. [I even wrote a blog post on it](https://franciscojavierarceo.github.io/post/docker-for-data-science).

Here's a one liner to get you up and running with Jupyter on any computer with Docker installed.

```
docker run -it -p 8888:8888 --rm -e JUPYTER_ENABLE_LAB=yes -v ~/Github/Python/:/home/jovyan/work jupyter/datascience-notebook
```
Useful links:

https://hub.docker.com/r/jupyter/datascience-notebook/

https://medium.com/codex/how-to-set-up-and-run-python-data-science-development-environment-with-jupyter-on-docker-17e04e11d6c

https://github.com/jupyter/docker-stacks
