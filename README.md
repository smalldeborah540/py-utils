# py-utils

Small Python helpers I found myself rewriting.

## Modules

- `retry.py` - exponential backoff decorator
- `files.py` - path helpers

## Usage

```python
from retry import retry

@retry(tries=3)
def flaky():
    ...
```

## Testing

```bash
pytest -q
```
