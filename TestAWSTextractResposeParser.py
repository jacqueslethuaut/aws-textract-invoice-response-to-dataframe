import os
import json
import boto3
import textractprettyprinter
import trp.trp2_expense as texp
import t_reko_expense as trexp

from textractprettyprinter.t_pretty_print_expense import get_string
from textractprettyprinter.t_pretty_print_expense import Textract_Expense_Pretty_Print, Pretty_Print_Table_Format
from trp import Document
from trp.trp2 import TDocument, TDocumentSchema

try:
    document = 'data/analyzeExpenseResponse.json'
    with open(document, 'r') as f:
        print(f)
        r = json.load(f)
        # print(r)


    pretty_printed_string = get_string(textract_json=r, 
                                       output_type=[Textract_Expense_Pretty_Print.SUMMARY, Textract_Expense_Pretty_Print.LINEITEMGROUPS], 
                                       table_format=Pretty_Print_Table_Format.fancy_grid)
    print(pretty_printed_string)    
    
    df = trexp.get_dataframe(r)
    print(df)
    print('Sum of VERIFICATION column : ', "{:.2f}".format(df['VERIFICATION'].sum()))

except Exception as e_raise:
    print(e_raise)
    raise e_raise