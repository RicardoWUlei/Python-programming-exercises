class myError(Exception):
    def __init__(self, msg):
        self.msg = msg

error = myError("sth wrong!")