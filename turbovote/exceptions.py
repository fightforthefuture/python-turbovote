class TurboVoteException(Exception):
    def __init__(self, message, errors):
        self.errors = set(errors)
        self.message = ', '.join(self.errors)
        Exception.__init__(self, self.message)
