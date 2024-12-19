# Receipts POC - System Design

## Simplifications

## Services

actor|service|label|db|q|
-----|-------|-----|--|-|
merchant|pos checkout|merchant_pos|db|-|
payment processor|new pmt|pmt_proc_new_pmt|db|-|
issuing bank|new pmt|iss_bank_new_pmt|db|-|
platform|new receipt|platform_new_receipt|db|q|
platform|new payment|platform_new_pmt|db|q|