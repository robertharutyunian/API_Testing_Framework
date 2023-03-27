class Config:

    """This class provides us with the base url and port according to the '--env' additional argument
    that we provide. The default '--env' value is 'local'."""

    def __init__(self, env):
        self.base_url = {
            "local": "https://localhost/"
        }[env]
        self.app_port = {
            "local": ":80"
        }[env]
