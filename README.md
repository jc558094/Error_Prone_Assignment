# Error Prone Assignment
There are 17 Bugs across both files:

14 in error_code.py

3 in error_code_functions.py

Line 5
from error_code_functions import combat, createMonster  -->
from error_code_functions import combat, create_monster

Line 90
            print(f"You were slain by the {monster["name"]}!") 
to
            print(f"You were slain by the {monster[__name__]}!") 



