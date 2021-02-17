"""
GENERAL INSTRUCTIONS
WARNING: For Python beginners:
the instructions here will only make sense after you have gone through and
completed the training materials.

1. WHICH PART TO CHANGE?: Uncomment every line with  [YOUR CODE HERE] and replace it with your code.
Please don't change anything else other than these lines.

2. USE OF JUPYTER NOTEBOOK: For those who would like to use Jupyter Notebook. You can copy and paste
each function in the notebook environment, test your code their. However,
remember to paste back your code in a .py file and ensure that its running
okay.

3. INDENTATION: Please make sure that you check your identation

4. Returning things frm function: All the functions below have to return a value.
Please dont forget to use the return statement to return a value.

5. HINTS: please read my comments for hints and instructions where applicable
"""


# import Python libraries if required

def return_element_of_a_list(list_of_things, i):
    """
    Return the i-th item of the list
    Example:
    Given list ['a', 'X', 'z'] and i: 2, the function returns 'z'
    :param i: Index of the item to return
    :return:
    """
    # use list indexing to get the ith item
    element =  list_of_things[i]

    # return the item
    return element


def calculate_average(list_of_numbers):
    """
    The function takes in a list of numbers and returns their mean.
    Example
    Given list [1, 2, 3]), the function returns 2
    :param list_of_numbers:A list of numbers
    :return:
    """

    # calculate  the sum using for loop
    # [YOUR CODE HERE]

    # get the length of the list of numbers using list function len()
    # [YOUR CODE HERE]

    # finally calculate the mean
    # [YOUR CODE HERE]

    # return the mean
    # [YOUR CODE HERE]


def concatenate_strings(first_name, last_name):
    """
     Given a persons first and last name, return a combined
     full name with space in between them.
     Example
     Given first name: 'Dunstan' and last name 'Matekenya' the function
     returns 'Dunstan Matekenya'. Note that there need to be space in between
    :param first_name: A string variable for first name
    :param last_name: A string variable for first name
    :return:
    """

    # use string concatenation to combine the two strings
    # [YOUR CODE HERE]


def check_if_list_contains_item(list_of_things, item):
    """
    Given a list, check if item is in the list, return 'YES' if
    thats the case and return NO if not
    Example
    Given list ['a', 'X', 'z'] and item 'M' the function should
    return  'NO'
    :param list_of_things:
    :param item:
    :return:
    """

    # use if and other conditional statements to check for membership
    # [YOUR CODE HERE]

    # return your result
    # [YOUR CODE HERE]


def count_number_of_csv_files(input_folder=None):
    """
    The function should return number of CSV files in a given folder
    :param input_folder:
    :return:
    """

    # use the os module to list all files in the folder and put them in a list
    # [YOUR CODE HERE]

    # use for loop, list indexing and if conditional statement to get the result
    # [YOUR CODE HERE]

    # return the result
    # [YOUR CODE HERE]


def save_list_to_csv(lst=None, csvfile_path=None):
    """
    Given a list (which can be nested), write elements of the list to a CSV file.
    Example
    Given list = ['a', 'X', 'z'], the CSV file will will have one row like this:
    'a', 'X', 'z'
    Given list = [['a', 'X', 'z'], ['1', '2', '3']], CSV file will have two rows
    like below:
    'a', 'X', 'z'
    '1', '2', '3'
    :param lst: List with items to write. Note that it can be a nested list
    :param csvfile_path: full path of CSV file, when testing, dont forget extension
    :return:
    """
    # to avoid some problems later, lets remove the file if it exist
    # use if statement and function 'remove()' from os module to achiev this
    # [YOUR CODE HERE]

    # open file object for writing with option "w+"
    # [YOUR CODE HERE]

    # how you write depends on whether the list is nested or not
    # to check is list is nested, use function "isinstance()" to check
    # if elements of the list are also lists
    # [YOUR CODE HERE]

    # close file object
    # [YOUR CODE HERE]

# define a function, please call it: report_basic_data_properties
# the function should take as input a CSV file, call the input
# parameter "csv_file"
# and return the following properties about the data
# 1. Number of rows in the data
# 2. List of column names
# Note that you can return two values in a function
# using a tuple


def get_name_of_town_with_highest_elevation(csv_file=None, elev_col="elev_metres"):
    """
    Given the following data file: day2-python-for-data-science/data/townships_with_dist_and_elev.csv
    return the town with highest elevation.
    Note that column name with elevation values is already provided as a default parameter.
    :param csv_file: CSV file with elevation data
    :param elev_col: Column with elevation values
    :return: town name with highest elevation value
    """
    # read data into pandas dataframe
    # [YOUR CODE HERE]

    # get the maximum value for elev_metres column
    # [YOUR CODE HERE]

    # inspect the object type which you get above
    # if its a series object use the function
    # "values" on it like so: pd_series.values
    # in order to get a string
    # [YOUR CODE HERE]

    # return the answer
    # [YOUR CODE HERE]


def plot_a_numeric_attribute(csv_file=None, col_to_plot=None, output_plot=None):
    """
    Given a CSV file, read the data using pandas, plot a given column
    and finally save the plot as "png" file.
    DATA FOR TESTING: day2-python-for-data-science/data/townships_with_dist_and_elev.csv
    COLUMN NAME FOR TESTING: 'elev_meters' column
    :param csv_file: File to get data from
    :param col_to_plot: Column name to plot
    :param output_plot: Save output plot to file
    :return:
    """

    # read data into pandas dataframe
    # [YOUR CODE HERE]

    # use seaborn to plot distribution of data
    # ax = sns.distplot(ADD YOUR CODE HERE)

    # save plot as png file
    # ax.get_figure().savefig(ADD YOUR CODE HERE)