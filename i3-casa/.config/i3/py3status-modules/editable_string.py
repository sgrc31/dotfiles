class Py3status:

    initial_text = "Non modificat"

    def __init__(self):
        self.full_text = None

    #def post_config_hook(self):
    #    self.full_text = self.initial_text

    def editable_string(self):
        if not self.full_text:
            self.full_text = self.initial_text
        return {
            "full_text": self.full_text,
            "chached_until": self.py3.CACHE_FOREVER
            }

    def on_click(self, event):
        mod_string = "modificato"
        self.full_text = self.py3.safe_format(mod_string)

