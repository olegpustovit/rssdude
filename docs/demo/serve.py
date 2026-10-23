# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

handler = partial(SimpleHTTPRequestHandler, directory=str(Path(__file__).parent))
print("Serving the fictional feed at http://127.0.0.1:18784/feed.xml")
ThreadingHTTPServer(("127.0.0.1", 18784), handler).serve_forever()
