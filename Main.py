from Pass_Func import *

#Initial Function Call
main()

#While loop for triggering re-runs
while True:
    run_again = pyip.inputYesNo("Would you like to check another password? (y/n)")
    if run_again == "yes":
        #Rerun main function
        main()
    else:
        print("Thanks for keeping your passwords secure!")
        break