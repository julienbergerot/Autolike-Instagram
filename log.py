import sys
from datetime import datetime
import time
import pyttsx3

old_out = sys.stdout

daily_file = "InstagramLikes_{}.txt".format(str(datetime.now().strftime("%d/%m/%Y")).replace("/","_"))

class St_ampe_dOut:
    """Stamped stdout."""
    nl = True

    def write(self, x):
        """Write function overloaded."""
        
        if x == '\n':
            old_out.write(x)
            self.nl = True
        elif self.nl:
            old_out.write("{} > {}".format(str(datetime.now())[:-7],x))
            with open("./logs/{}".format(daily_file), "a") as f :
                f.write("{} > {} \n".format(str(datetime.now())[:-7],x))
            self.nl = False
        else:
            old_out.write("{} > {}".format(str(datetime.now())[:-7],x))
            with open("./logs/{}".format(daily_file), "a") as f :
                f.write("{} > {} \n".format(str(datetime.now())[:-7],x))
        
sys.stdout = St_ampe_dOut()