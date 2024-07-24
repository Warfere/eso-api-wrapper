
# Eso api wrapper

## In this README :point_down:

- [Features](#features)
- [Usage](#usage)
  - [Initial setup](#initial-setup)
  - [Creating releases](#creating-releases)
- [FAQ](#faq)
- [Contributing](#contributing)

## Features

This template repository comes with all of the boilerplate needed for:

⚙️ Robust (and free) CI with [GitHub Actions](https://github.com/features/actions):
  - Unit tests ran with [PyTest](https://docs.pytest.org) against multiple Python versions and operating systems.
  - Type checking with [mypy](https://github.com/python/mypy).
  - Linting with [pylint](https://www.pylint.org/).
  - Formatting with [black](https://black.readthedocs.io/en/stable/).

## Usage

### Initial setup

First you have to register for api_key and whitelist your IP.
https://www.eso.lt/web/api-paslaugos-uzsakymas/307

Install package

```bash
pip install eso_api
```
after installing
```python
from eso_api import EsoApi,Headers

eso = EsoApi(Headers(api_key=API_KEY))
date = datetime(2024, 3, 1, 0, 0, 0)
response = eso.get_obejects(date)
```

In case of some issues, server will return 200 but will have body:
```json
{"statusCode": 401, "message": "Access denied due to invalid subscription key. Make sure to provide a valid key for an active subscription."}
```

## Contributing

If you find a bug :bug:, please open a [bug report](https://github.com/allenai/python-package-template/issues/new?assignees=&labels=bug&template=bug_report.md&title=).
If you have an idea for an improvement or new feature :rocket:, please open a [feature request](https://github.com/allenai/python-package-template/issues/new?assignees=&labels=Feature+request&template=feature_request.md&title=).
