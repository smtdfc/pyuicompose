class ContextError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(f"[PyUIComposeError.ContextError] {message}")
