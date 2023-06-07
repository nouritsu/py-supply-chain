class Result:
    _ok: any
    _err: str

    def __init__(self):
        self._ok = None
        self._err = None

    # Get sucess return
    def ok(self) -> any:
        return self._ok

    # Get error message
    def err(self) -> str:
        return self._err

    # Check if result has an error
    def is_err(self) -> bool:
        return self._err != None

    # Don't use this function
    def _set_ok(self, x: any):
        self._ok = x

    # Don't use this function
    def _set_err(self, msg: str):
        self._err = msg

    def __repr__(self):
        return f"<Result (Ok: {self._ok} ,Err: {self._err})>"

    def __str__(self):
        return self.__repr__()
