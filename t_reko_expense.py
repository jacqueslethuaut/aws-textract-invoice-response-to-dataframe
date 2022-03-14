import pandas as pd
import logging
import sys
import numpy as np
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

from textractprettyprinter.t_pretty_print_expense import get_expensesummary_string
from textractprettyprinter.t_pretty_print_expense import get_expenselineitemgroups_string
from textractprettyprinter.t_pretty_print_expense import Textract_Expense_Pretty_Print, Pretty_Print_Table_Format

logger = logging.getLogger(__name__)

def get_dataframe(txt_json:dict):
    """
    Main method for the clients to call for pretty printing the AnalyzeExpense Response
    """
    # str1 = get_expensesummary_string(textract_json=txt_json, table_format=Pretty_Print_Table_Format.csv)
    # print(str1)
            
    str2 = get_expenselineitemgroups_string(textract_json=txt_json, table_format=Pretty_Print_Table_Format.csv)
    # print(str2)

    df1 = pd.read_csv(StringIO(str2), sep=",")
    df2 = pd.DataFrame(np.vstack([df1.columns, df1]))
    df2.columns = ['ITEM', 'QUANTITY', 'PRICE', 'TOTAL']
    df2['ITEM'] = df2['ITEM'].map(lambda x: x.rstrip('(ITEM)'))
    df2['QUANTITY'] = df2['QUANTITY'].map(lambda x: x.rstrip('(QUANTITY)'))
    df2['PRICE'] = df2['PRICE'].map(lambda x: x.rstrip('(OTHER)'))
    df2['TOTAL'] = df2['TOTAL'].map(lambda x: x.rstrip('T(PRICE)'))
    df2[df2.columns[1:]] = df2[df2.columns[1:]].replace('[\$,]', '', regex=True).astype(float)
    verif = df2.QUANTITY * df2.PRICE
    df2['VERIFICATION'] = verif
    
    return df2

