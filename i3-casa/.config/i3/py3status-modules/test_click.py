# -*- coding: utf-8 -*-
"""
Example module that handles events

This demonstrates how to use events.
"""


class Py3status:

    def __init__(self):
        self.full_text = 'Click me'

    def click_info(self):
        return {
            'full_text': self.full_text,
            'cached_until': self.py3.CACHE_FOREVER
        }

    def on_click(self, event):
        """
        event will be a dict like
        {'y': 13, 'x': 1737, 'button': 1, 'name': 'example', 'instance': 'first'}
        """
        button = event['button']
        # update our output (self.full_text)
        format_string = 'You pressed button {button}'
        data = {'button': button}
        self.full_text = self.py3.safe_format(format_string, data)
        # Our modules update methods will get called automatically.
