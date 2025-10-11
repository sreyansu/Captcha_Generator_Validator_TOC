from server import app as flask_app
from vercel_wsgi import make_lambda_handler

# Vercel entry point: handler is discovered automatically
handler = make_lambda_handler(flask_app)
