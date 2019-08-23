import sys, variable
from service import Judgement
from utility import Calculation


class NewAPP:
    args = sys.argv
    try:
        CHECK_NUMBER1 = int(args[1])
        CHECK_NUMBER2 = int(args[2])

        SUM = Calculation.add(CHECK_NUMBER1,CHECK_NUMBER2)
        RESULT = Judgement.chenking(SUM)
       
    except ValueError:
        print(variable.VALLUE_ERROR)
    except IndexError:
        print(variable.INDEX_ERROR)

print(RESULT)
    

   
    
    