from src.Core.general.general import index
from src.Core.general.general import update

def dispacther():

    dispatch={
        "index":index,
        "update":update
    }
    return dispatch