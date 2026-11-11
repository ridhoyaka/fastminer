so i ran it with default settings and the app seems to get stuck when training, in the ui it would get stuck at training in progress, particularly in training gradient boosting

below is the terminal output
(.venv) aaaaa@laptop-h7x9:~/Workspace/sm5/datamining_sm5/proyek apk$ dc web
Starting Data Classifier web app at http://127.0.0.1:5000
Paths:
  data/uploads/  - uploaded files
  models/        - saved models
  reports/       - outputs & inspection reports
  .web_data/     - history database (SQLite)
Press Ctrl+C to stop
 * Serving Flask app 'dc.web.app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [30/Oct/2026 14:45:53] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:45:53] "GET /static/js/htmx.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:45:53] "GET /static/js/bootstrap.bundle.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:45:53] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:46:13] "GET /static/js/htmx.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:13] "GET /static/js/bootstrap.bundle.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:13] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:25] "POST /upload HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:46:25] "GET /static/js/htmx.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:25] "GET /static/js/bootstrap.bundle.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:25] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:32] "GET /explore HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:46:32] "GET /static/js/htmx.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:32] "GET /static/js/bootstrap.bundle.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:32] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:56] "POST /explore HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:46:56] "GET /static/js/bootstrap.bundle.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:56] "GET /static/js/htmx.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:46:56] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:47:01] "GET /train HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:01] "GET /static/js/htmx.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:47:01] "GET /static/js/bootstrap.bundle.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:47:01] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:47:08] "POST /train HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:08] "GET /static/css/bootstrap.min.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:47:08] "GET /static/js/htmx.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:47:08] "GET /static/js/bootstrap.bundle.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Oct/2026 14:47:08] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:09] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:10] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
[2026-10-30 14:47:11,209] ERROR in app: Exception on /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 [GET]
Traceback (most recent call last):
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 920, in full_dispatch_request
    return self.finalize_request(rv)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 941, in finalize_request
    response = self.process_response(response)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 1322, in process_response
    self.session_interface.save_session(self, ctx._session, response)
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/sessions.py", line 373, in save_session
    val = self.get_signing_serializer(app).dumps(dict(session))  # type: ignore[union-attr]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/serializer.py", line 316, in dumps
    payload = want_bytes(self.dump_payload(obj))
                         ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/url_safe.py", line 56, in dump_payload
    json = super().dump_payload(obj)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/serializer.py", line 278, in dump_payload
    return want_bytes(self.serializer.dumps(obj, **self.serializer_kwargs))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/tag.py", line 323, in dumps
    return dumps(self.tag(value), separators=(",", ":"))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/__init__.py", line 41, in dumps
    return current_app.json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/provider.py", line 179, in dumps
    return json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 238, in dumps
    **kw).encode(obj)
          ^^^^^^^^^^^
  File "/usr/lib/python3.12/json/encoder.py", line 200, in encode
    chunks = self.iterencode(o, _one_shot=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/encoder.py", line 258, in iterencode
    return _iterencode(o, 0)
           ^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/provider.py", line 121, in _default
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
TypeError: Object of type Pipeline is not JSON serializable
[2026-10-30 14:47:11,213] ERROR in app: Request finalizing failed with an error while handling an error
Traceback (most recent call last):
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 920, in full_dispatch_request
    return self.finalize_request(rv)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 941, in finalize_request
    response = self.process_response(response)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 1322, in process_response
    self.session_interface.save_session(self, ctx._session, response)
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/sessions.py", line 373, in save_session
    val = self.get_signing_serializer(app).dumps(dict(session))  # type: ignore[union-attr]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/serializer.py", line 316, in dumps
    payload = want_bytes(self.dump_payload(obj))
                         ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/url_safe.py", line 56, in dump_payload
    json = super().dump_payload(obj)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/serializer.py", line 278, in dump_payload
    return want_bytes(self.serializer.dumps(obj, **self.serializer_kwargs))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/tag.py", line 323, in dumps
    return dumps(self.tag(value), separators=(",", ":"))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/__init__.py", line 41, in dumps
    return current_app.json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/provider.py", line 179, in dumps
    return json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 238, in dumps
    **kw).encode(obj)
          ^^^^^^^^^^^
  File "/usr/lib/python3.12/json/encoder.py", line 200, in encode
    chunks = self.iterencode(o, _one_shot=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/encoder.py", line 258, in iterencode
    return _iterencode(o, 0)
           ^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/provider.py", line 121, in _default
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
TypeError: Object of type Pipeline is not JSON serializable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 941, in finalize_request
    response = self.process_response(response)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/app.py", line 1322, in process_response
    self.session_interface.save_session(self, ctx._session, response)
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/sessions.py", line 373, in save_session
    val = self.get_signing_serializer(app).dumps(dict(session))  # type: ignore[union-attr]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/serializer.py", line 316, in dumps
    payload = want_bytes(self.dump_payload(obj))
                         ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/url_safe.py", line 56, in dump_payload
    json = super().dump_payload(obj)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/itsdangerous/serializer.py", line 278, in dump_payload
    return want_bytes(self.serializer.dumps(obj, **self.serializer_kwargs))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/tag.py", line 323, in dumps
    return dumps(self.tag(value), separators=(",", ":"))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/__init__.py", line 41, in dumps
    return current_app.json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/provider.py", line 179, in dumps
    return json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 238, in dumps
    **kw).encode(obj)
          ^^^^^^^^^^^
  File "/usr/lib/python3.12/json/encoder.py", line 200, in encode
    chunks = self.iterencode(o, _one_shot=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/encoder.py", line 258, in iterencode
    return _iterencode(o, 0)
           ^^^^^^^^^^^^^^^^^
  File "/home/aaaaa/.local/lib/python3.12/site-packages/flask/json/provider.py", line 121, in _default
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
TypeError: Object of type Pipeline is not JSON serializable
127.0.0.1 - - [30/Oct/2026 14:47:11] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 500 -
127.0.0.1 - - [30/Oct/2026 14:47:12] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:13] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:14] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:15] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:17] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:18] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:19] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:20] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:21] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:22] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:23] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:24] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:25] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:26] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:27] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:28] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:29] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:30] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:31] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:32] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:33] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:34] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:35] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:36] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:37] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:38] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:39] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:40] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:41] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:42] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:43] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:44] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:45] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:46] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:47] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:48] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:49] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:50] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:51] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:52] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:53] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:54] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:55] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:56] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:57] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:58] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:47:59] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:00] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:01] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:02] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:03] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:04] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:05] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:06] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:07] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:08] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:09] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:10] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:11] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:12] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:13] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:14] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:15] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:16] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:17] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:18] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:19] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:20] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:21] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:22] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:23] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:24] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:25] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:26] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:27] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:28] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:29] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:30] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:31] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:32] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:33] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:34] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:35] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:36] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:37] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:38] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:39] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:40] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:41] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:42] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:43] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:44] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:45] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:46] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:47] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:48] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:49] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:50] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:51] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:52] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:53] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:54] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:55] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:56] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:57] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:58] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:48:59] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:00] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:01] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:02] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:03] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:04] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:05] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:06] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:07] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:08] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:09] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:10] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:11] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:12] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:13] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:14] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:15] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:16] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:17] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:18] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:19] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:20] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:21] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:22] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:23] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:24] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:25] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:26] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:27] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:28] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:29] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:30] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:32] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:33] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:34] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:35] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:36] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:37] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:38] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:39] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:40] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:41] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:42] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:43] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:44] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:45] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:46] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:47] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:48] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:49] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:50] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:51] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:52] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:53] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:54] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:55] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:56] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:57] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:58] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:49:59] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:00] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:01] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:02] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:03] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:04] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:05] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:06] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:07] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:08] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:09] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:10] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:11] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:12] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:13] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:14] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:15] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2026 14:50:16] "GET /train/status/207ed179-f0bb-4f9b-b2db-a368c4a3ac14 HTTP/1.1" 200 -
1