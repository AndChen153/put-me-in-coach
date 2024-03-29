"""Welcome to Reflex!."""

from webapp import styles

# Import all the pages.
from webapp.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)
app.api.add_api_route("/terrawebhook", api_test, methods=['POST'])