# aws-textract-invoice-response-to-dataframe
AWS Textract invoice response to dataframe

Just a little exmaple to retrieve AWS textract expense analysis into a dataframe

analyzeExpenseResponse.json is the json response from AWS Textract

here is the str output from mazon-textract-prettyprinter

╒═══════════════════════════════════╤═════════════════╕
│ Key                               │ Value           │
├───────────────────────────────────┼─────────────────┤
│ (VENDOR_NAME)                     │ DB SHOES - RENO │
├───────────────────────────────────┼─────────────────┤
│ Cashier:(OTHER)                   │ Icw             │
├───────────────────────────────────┼─────────────────┤
│ Store:(OTHER)                     │ REN             │
├───────────────────────────────────┼─────────────────┤
│ Debit Card:(OTHER)                │ $64.62          │
├───────────────────────────────────┼─────────────────┤
│ Phone:(OTHER)                     │ (775)996-1900   │
├───────────────────────────────────┼─────────────────┤
│ TOTAL:(TOTAL)                     │ $64.62          │
├───────────────────────────────────┼─────────────────┤
│ Sales Receipt(INVOICE_RECEIPT_ID) │ #108772         │
├───────────────────────────────────┼─────────────────┤
│ Subtotal:(SUBTOTAL)               │ $59.99          │
├───────────────────────────────────┼─────────────────┤
│ 7.725% Tax:(TAX)                  │ + $4.63         │
╘═══════════════════════════════════╧═════════════════╛

╒═══════════════════════╤═════════════╤═══════════════╤═════════════════╕
│ 10166                 │ 1(QUANTITY) │ $20.00(OTHER) │ $20.00 T(PRICE) │
│ LTO KP PURE 2KS(ITEM) │             │               │                 │
├───────────────────────┼─────────────┼───────────────┼─────────────────┤
│ 10166(ITEM)           │ 1(QUANTITY) │ $20.00(OTHER) │ $20.00 T(PRICE) │
├───────────────────────┼─────────────┼───────────────┼─────────────────┤
│ LTO KP PURE 2KS       │ 1(QUANTITY) │ $19.99(OTHER) │ $19.99 T(PRICE) │
│ 11899(ITEM)           │             │               │                 │
╘═══════════════════════╧═════════════╧═══════════════╧═════════════════╛

Here is the dataframe (VERIFICATION is the added column for verification = QUANTITY*PRICE)

                     ITEM  QUANTITY  PRICE  TOTAL  VERIFICATION
0  10166\nLTO KP PURE 2KS       1.0  20.00  20.00         20.00
1                   10166       1.0  20.00  20.00         20.00
2  LTO KP PURE 2KS\n11899       1.0  19.99  19.99         19.99
Sum of VERIFICATION column :  59.99