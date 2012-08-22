class TurboVoteException(Exception):
    def __init__(self, message, errors):
        self.errors = errors
        self.message = ', '.join(self.errors)
        Exception.__init__(self, self.message)
