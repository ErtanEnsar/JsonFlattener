import sys
import json

class JsonFlattener:
    """
    A class used to flatten nested jsons
    ...
    Attributes
    ----------
    Return_value : Dictionary
        a dictionary which serves as a temporary variable for the recursive nested output
    Methods
    -------
    data_loader_sanitizer()
        Receives input via stdin and makes sure it's valid Json.
    flatten(data)
        Flattens nested Json objects
    """
    def __init__(self):
        self.Return_value = {}

    def data_loader_sanitizer(self):
        """Receives input via stdin and makes sure it's valid Json.
        Raises
        ------
        IndexError
        If input is out of bounds
        Exception
        If input is not valid Json
        """
        try:
            fileobj = open(sys.argv[1], 'r')
        except IndexError:
            fileobj = sys.stdin
        with fileobj:
            data = fileobj.read()

        try:
            data = json.loads(data)
        except:
            print("Failure decoding Json, Syntax Error")
            quit()
        return data


    def flatten(self,Json_object, Nested_name=''):
        """ Flattens nested Json objects
        Parameters
        ----------
        Json_object:Dict
            The Json object to be flattened
        Nested_name:str
            To be used by the function itself to replace key name
        """
        if type(Json_object) == dict:
            for key in Json_object:
                self.flatten(Json_object[key], Nested_name + key + '.')
        else:
            self.Return_value[Nested_name[:-1]] = Json_object
        data= json.dumps(self.Return_value, indent=1)
        return data

    def flush(self):
        """ Flushes the temporary Return_value
        """
        self.Return_value.clear()
