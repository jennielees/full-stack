"""test.py

   First-run test for students to confirm their environment is
   working as intended.

   jennie@hackbrightacademy.com
   september 2014
"""

def main():
    """This is a function called "main". Its sole reason for existence
       is to neatly wrap up the code we want to run when we type
       `python test.py`.
    """

    # print by itself just prints an empty line.
    print
    print " ========================= "
    print " HACKBRIGHT BACK-END CLASS "
    print " ========================= "

    print
    print " Awesome, your environment is working!"

    print " Go to http://labs.bewd.co in a browser to continue."
    print

    result = raw_input(" -- Hit Y when the page has loaded...")

    result_valid = False

    if result == "Y":
        result_valid = True
    elif result == "":
        print " Just hit Enter? I suppose that'll do."
        result_valid = True
    else:
        print " I asked for 'Y', but I'll take " + result + "."
        result_valid = True

    if result_valid:
        print
        print " The password to the page is LABRADOR"
        print " Go forth, and Python on!"
        print


if __name__=="__main__":
    """This translates to "If this file is run directly from the
       command-line, do what follows."
    """
    main()