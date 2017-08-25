# Pypi package builder for Lighthouse Slack Bot

It is a package builder for distributing [oglhslack](https://github.com/opengeardev/oglhslack) throught Pypi.

For uploading a new version it is necessary to update the versions inside `setup.py`, something like:

```python
version = '0.1.5'
```

In case of a change in the [oglhslack](https://github.com/opengeardev/oglhslack), it is also necessary to update the `download_url` variable in `setup.py` for matching the proper release.

## Uploading

For uploading a new version:

```bash
$ git submodule update --remote
$ pandoc --from=markdown --to=rst --output=README.rst oglhslack/README.md
$ python setup.py sdist upload
```
