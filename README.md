# My first app in Flask

---

> ***v1.1*** - This is an initial project in a learning path.

*Some features*

- Models, views and forms in this project are in same file.

- It include error handler for 404 and 500 errors.

- The project include some tests.

- It uses templates for views with template inheritance and jinja 2.

- The project doesn't use (currently) any database.

## Versions

```
Flask 2.1.3
Flask-Bootstrap 3.3.7.1
Flask-Testing 0.8.1
Flask-WTF 1.0.1
```

You can see complete list in [requirements.txt](requirements.txt)

---
---

# How to run this app in localhost?

1. Create and activate your virtualenv with python version 3.8.10

2. Run

```
pip install -r requirements.txt
```

3. Run

```
./flask_script.sh
```

This command run `flask run`... remember to chmod with 774 like this `sudo chmod 774 flask_script.sh`

**Environment variable**

    For debugging mode: `FLASK_DEBUG=1`
    For work in development environment: `FLASK_ENV=development`
    For define main file: `FLASK_APP=main.py`

## How to run tests

```
flask test
```

**Note:**
[you might have to edit this for assert redirect comparisons:](https://pastebin.com/7CLNGK0h) (credits to the author: Carlos Castro in Platzi web page).

```python
    def assertRedirects(self, response, location, message=None):
        parts_location = urlparse(location)

        valid_status_codes = (301, 302, 303, 305, 307)
        valid_status_code_str = ', '.join(str(code) for code in valid_status_codes)
        not_redirect = "HTTP Status %s expected but got %d" % (valid_status_code_str, response.status_code)
        self.assertTrue(response.status_code in valid_status_codes, message or not_redirect)

        if parts_location.netloc:
            expected_location = location
        else:
            server_name = self.app.config.get('SERVER_NAME') or 'localhost'
            expected_location = urljoin("http://%s" % server_name, location)
            # expected_location = location

        parts_response = urlparse(response.location)

        if parts_response.netloc:
            self.assertEqual(response.location, expected_location, message)
        else:
            server_name = self.app.config.get('SERVER_NAME') or 'localhost'
            response_url = urljoin("http://%s" % server_name, location)
            self.assertEqual(response_url, expected_location, message)
```
