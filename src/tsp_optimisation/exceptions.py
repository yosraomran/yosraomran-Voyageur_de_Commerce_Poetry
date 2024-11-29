class ContrainteNonSatisfaiteException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class DonneesInvalidesException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class CalculErreurException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
