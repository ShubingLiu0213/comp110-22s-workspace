"""Dictionary related utility functions."""

__author__ = "730508266"
from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = [] 
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row) 
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    
    return result


def head(data_cols: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only first N rows."""
    result: dict[str, list[str]] = {}
    parameter: list[str] = []
    if rows > len(data_cols):
        return data_cols
    
    for key in data_cols:
        parameter = []
        i: int = 0
        while i < rows:
            parameter.append(data_cols[key][i])
            i += 1
        result[key] = parameter
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    parameter: list[str] = []
    for key in table:
        i: int = 0
        while i < len(names):
            if key == names[i]:
                for values in table[key]:
                    parameter.append(values)
                    result[key] = parameter
                    i += 1
            else:
                i += 1
        parameter = []
    return result
        

def concat(data_cols_head: dict[str, list[str]], additional_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in data_cols_head:
        result[key] = data_cols_head[key]
       
    for key in additional_table:
        if key in result:
            result[key] = result[key] + additional_table[key]
        else:
            result[key] = additional_table[key]

    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appeared in the input list."""
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def helper(data: dict[str, int]) -> int:
    """ Rearranging the data according to the order of the key."""
    temp: dict[int, int] = {}
    new_data: dict[str, int] = {}
    result: int = 0
    for i in data:
        temp[int(i)] = data[i]
        if int(i) >= 5:
            new_data[i] = temp[int(i)]
    for k in new_data:
        result += new_data[k]
    return result
    
