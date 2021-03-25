class Action:
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast, args, director):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            args (dict): The specific event arguments like key pressed, etc.
            director (Director): An instance of director.
        """
        raise NotImplementedError("execute not implemented in superclass")