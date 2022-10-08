# adilytics

![example branch parameter](https://github.com/team-12-csc-510/adilytics/actions/workflows/main.yml/badge.svg?branch=main)
[![PyPI - License](https://img.shields.io/pypi/l/FastAPI)](https://opensource.org/licenses/MIT)
![Made By](https://img.shields.io/badge/Made_By-Python3.9-green)
[![codecov](https://codecov.io/gh/team-12-csc-510/adilytics/branch/main/graph/badge.svg?token=TKKWAHLJIO)](https://codecov.io/gh/team-12-csc-510/adilytics)
[![DOI](https://zenodo.org/badge/540565328.svg)](https://zenodo.org/badge/latestdoi/540565328)
[![Issues_Open](https://img.shields.io/github/issues-raw/team-12-csc-510/adilytics)](https://github.com/team-12-csc-510/adilytics/issues?q=is%3Aopen+is%3Aissue)
[![Issues_Closed](https://img.shields.io/github/issues-closed/team-12-csc-510/adilytics)](https://github.com/team-12-csc-510/adilytics/issues?q=is%3Aissue+is%3Aclosed)

<p>
  <a href="">
    <img src="/media/adylitics_logo.jpeg" alt="Logo" height="400" width="600"/>
  </a>
</p>

# Project 1: Perform the advertisement analytics on a platform and visualise the results.

Team 12's submission for Project 1 for CSC-510.

## Here is a quick introduction video:

https://user-images.githubusercontent.com/112341004/194640685-1cfeffa0-c33c-4c2f-b2c5-de64d47c637a.mp4

## Table Of Contents

- [Installation](#installation)
- [License](#license)
- [Tools](#tools)
- [Team](#team)

______________________________________________________________________

## Installation

Requires [Python] v3.9+.
Clone the repository and move into the project directory and install the project dependencies. <br>

To install the dependencies/packages required for the project install [Poetry]

```shell
curl https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
```

To get started you need [Poetry]'s bin directory `(/Users/<username>/Library/Python/python-version/bin)` in your `PATH`
environment variable.

> Refer [here](https://stackoverflow.com/questions/60768676/what-is-the-default-install-path-for-poetry) for configuring poetry path correctly.

You can test that everything is set up by executing:

```shell
poetry --version
```

Configure [Poetry] virtual environment by

```shell
poetry env use python3
poetry install
```

______________________________________________________________________

## License

This project is licensed under MIT license available in [LICENSE](https://github.com/team-12-csc-510/hw1/blob/main/LICENSE.md) file

______________________________________________________________________

## Tools

<ins>**Fast Api**</ins>

This project makes use of FAST API.
You can refer to the link to learn more about its working [FAST API](https://fastapi.tiangolo.com) .

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

Some key features are:

- **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](#performance).
- **Fast to code**: Increase the speed to develop features by about 200% to 300%.
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors.
- **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (previously known as Swagger) and <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<ins>**Locust**</ins>

This project makes use of Locust.
You can refer to the link to learn more about its working [Locust](https://docs.locust.io/en/stable/installation.html).

Locust is used to run load tests distributed over multiple machines. It is event-based (using [gevent](http://www.gevent.org/)), which makes it possible for a single process to handle many thousands concurrent users. While there alternatives capable of doing more requests per second on a given hardware, the low overhead of each Locust user makes it very suitable for testing highly concurrent workloads.

______________________________________________________________________

## Team

Name  | Unity id
------------- | -------------
Aditya Tewari  | adtewari
Naman Bhagat  | nbhagat2
Ritwik Tiwari  | rtiwari2
Saksham Thakur  | sthakur5
Shubhender Singh  | ssingh54

______________________________________________________________________

[poetry]: https://python-poetry.org/
[python]: https://python.org
