#!/usr/bin/env python3

class Error(Exception):
    """Main parent error class
    """
    def __init__(self, message):
        """Constructor
        Args:
            message: the error message as a string
        """
        self.message = message
        super().__init__(self.message)
