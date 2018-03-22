
import logging

# ------------------- global constants -------------------------
#
CAT_TYPE_ALLOTHER = 'allother'  # Category type
REL_TYPE_ARITHMETIC_SEQUENCE = 'arithmetic_sequence'  # Relation type
REL_TYPE_GEOMETRIC_SEQUENCE = 'geometric_sequence'
REL_TYPE_EXPONENTIAL_SEQUENCE = 'exponential_sequence'
REL_TYPE_LOGARITHMIC_SEQUENCE = 'logarithmic_sequence'
REL_TYPE_UNKNOWN = 'unknown'

REL_TYPE_LIST_TO_ONE_SUM = 'list_to_one_sum'
REL_TYPE_LIST_TO_ONE_MAX = 'list_to_one_max'
REL_TYPE_LIST_TO_ONE_MIN = 'list_to_one_min'
REL_TYPE_LIST_TO_ONE_MEAN = 'list_to_one_mean'


# Error codes
ERROR_NOT_ARTHIMETIC_GEOMETRIC = "Sorry, I could not find any Arthimatic/Geometric relationship between Input & Output, Pls. check data!!!"
ERROR_LIST = [ERROR_NOT_ARTHIMETIC_GEOMETRIC, 1 ]


# ------------------- Relationship_data -------------------------
# class to hold category data
# -------------------  *****************-------------------
class Relationship_data(object):
    input_symbol = ''
    output_symbol = ''
    input2_symbol = ''
    relationship_type = ''
    value1 = ''
    value2 = 0
    value3 = ''

    def update_symbols(self, input_symbol, output_symbol, input2_symbol):
        self.input_symbol = input_symbol
        self.output_symbol = output_symbol
        self.input2_symbol = input2_symbol

    def update(self, relationship_type, val1, val2=0, val3=''):
        self.relationship_type = relationship_type
        self.value1 = val1
        self.value2 = val2
        self.value3 = val3


REL_OBJ = Relationship_data()  # create new global instance



# ------------------- Logging -------------------------
#
# -------------------  *****************-------------------

# https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings
def setup_logger(filename="/Users/padma/ddcBot/log/log-4-ddcBot.log"):

    logging.basicConfig(
        filename=filename,
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s"
        # level=logging.INFO,
        # format="%(asctime)s:%(levelname)s:%(message)s"
        )

    logger = logging.getLogger("ddcB")
    return logger

# Logging Tutorial : https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
log = setup_logger()


