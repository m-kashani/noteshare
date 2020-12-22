from src.Core.general.general import index
from src.Core.general.general import clear
from src.Core.general.general import update
from src.Core.general.general import find
def dispacther():

    dispatch={
        "index":index,
        "clear":clear,
        "update":update,
        "find":find
    }
    return dispatch