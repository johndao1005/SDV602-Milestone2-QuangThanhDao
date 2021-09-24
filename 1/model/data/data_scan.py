"""
Read csv file in data folder by defaul but also allow reading data from different file source 
"""
import sys as sys
from os import path
from typing import Dict

class DataManager():
    dict_list = []
    value_list = []
    def __init__(self) -> None:
        self.status:Dict = {}
        self.current_files:Dict = {}
        self.current_file = None
        
    def get_file(self,path_to_file):
        try:
            self.current_file = open(path_to_file)
            return self.current_file
        except FileNotFoundError:
            file_not_found = ("File not found error", path_to_file)
            self.status['File Error'] = [file_not_found] if not ('File Error' in self.status) else self.status['File Error'] + [file_not_found]
            return None
        except FileExistsError   :
            file_exists_error = ("File exists error", path_to_file)
            self.status['File Error'] =  [file_exists_error] if not ('File Error' in self.status) else self.status['File Error'] + [file_exists_error]
            return None 
        except:
            print("Unexpected error:", sys.exc_info()[0]) 
            return None
                
        
    def close_file(self,file_object) :
        file_object.close()

    def scan(self,filter= None, has_header=False, csv_file= sys.stdin):
        """
        Scans a csv, by default

        Args
        """
        result = []
        values = []
        do_header = has_header
        header_names = {}
        try:
            lines = [aline for aline in csv_file if filter(aline)] if filter != None else csv_file
            for aline in lines:
                    this_line = aline.strip().split(',')
                    if do_header:
                        header_names = this_line
                        print(f" header names {header_names}")
                        do_header = False
                    else:
                        a_dict = {}
                        i = 0
                        max_header_index = len(header_names) -1 
                        for column in this_line:
                            if has_header :
                                if i > max_header_index :
                                    break
                                
                                a_dict[header_names[i]]= column
                            else:
                                a_dict[i]= column
                            i = i + 1 

                        
                        result += [a_dict]
                        values += [this_line]
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return None,None

        DataManager.dict_list = result
        DataManager.value_list = values 
        return result,values


    def sum_of(self,column_name, a_list_of_dictionary):
        """
        Return one value that is the sum of the column 
        column_name of each "row" (dictionary)
        """
        running_sum = 0
        for row in a_list_of_dictionary:
            running_sum += row[column_name]
        return running_sum

            


    def multiplies_cols(self,column_names,a_list_of_dictionary):
        """
        Return a new list of "rows" (dictionary)
        That multiplies the values of the named columns
        
        """
        result_list = []
        for a_row in a_list_of_dictionary:
            row_product = 1
            for a_name in column_names:
                row_product *= a_row[a_name]
            result_list += [{'Mult':row_product}]    
        return result_list


    def display_table(self,a_list_of_dictionary):
        """
        Prints a table with a header - if there is no header the header becomes the column number.

        Args
                a_list_of_dictionary - each ite in the list is a Dictionary representing a Row in the table.
        """
        if a_list_of_dictionary != [] :
            lines = ""
            # Get a header line
            a_dictionary = a_list_of_dictionary[0]
            header_line = ""
            for key in a_dictionary:
                header_line += f'{key}\t'
            header_line = header_line.strip()

            # Make up the table
            lines += header_line 

            for a_dictionary in a_list_of_dictionary:
                a_line = ''
                for key,value in a_dictionary.items():
                    a_line += f'{value}\t'
                a_line = a_line.strip()
                lines += f'\n{a_line}'
            print(lines)
        else:
            print("No items to tabulate")

def line_col(x,num):
    c =  (x.strip().split(',')[num]).strip()
    print(c) 
    return c

if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser(description="Scan some rows into a list of one list per line.")
    parser.add_argument('--header',action='store_true',help='The first row is a header row.')
    args = vars(parser.parse_args())
    print(f'The args are {args}')
    #args = sys.argv
    #print(f'The args are {args}')
    dict_lst,values_lst = scan(args['header'])
    display_table(dict_lst)
    """
    csv_file_name = "data.csv"
    data_manager = DataManager()
    csv_file_obj = data_manager.get_file(csv_file_name)
    print(f" STATUS [{data_manager.status}]")
    if not('File Error') in data_manager.status:
        dict_lst,values_lst = data_manager.scan(filter=lambda line: '5' in [line_col(line,4)]  ,has_header = False,csv_file = csv_file_obj)
        data_manager.close_file(csv_file_obj)
        if not('File Error') in data_manager.status: data_manager.display_table(dict_lst)

       


