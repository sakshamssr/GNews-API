# GNews-API
A Fast and lightweight Python API that searches for articles on Google News and returns a JSON response.

## Search
Details regarding the usage of the search function.
```
https://gnewssapi.vercel.app/news/{query}
```

```python
import requests

# Using the example query "python".
url = "https://gnewssapi.vercel.app/news/python"
response = requests.get(url)
data = response.json()

print(data)

```
### Json Output Format:
```json
{
    {
    "id": {
        "title": "string",
        "updated_on": {
            "time": "HH:MM:SS",
            "date": "YYYY:MM:DD"
        },
        "link": "string"
    },
```
