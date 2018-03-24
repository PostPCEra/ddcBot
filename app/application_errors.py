
# ----------------------------  Application Errors --------------------------------------------------------------
# ------- This file lists all Application level error codes with descriptive forms -------------------------
# ------- This file is on it's own because these messages can be edited by non-technical team members product managers/Linguists
#

def msg(error_code):
    return error_code + ": " + eval(error_code)

E_IOL0_UNKONWN = 'some UNKNOWN exception occured'
E_IOL1_MISSING_WORDS = "@input @output Meta tags does not exist in proper format."
E_IOL2_SEPCHAR = 'The separator ; is missing in the input output legend'



# Error codes
ERROR_NOT_ARTHIMETIC_GEOMETRIC = "Sorry, I could not find any Arthimatic/Geometric relationship between Input & Output, Pls. check data!!!"
ERROR_LIST = [ERROR_NOT_ARTHIMETIC_GEOMETRIC, 1 ]


