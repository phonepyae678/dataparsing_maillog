# dataparsing_maillog
This is the program for finding given sender mail ID and recipient mail ID from sample 10_sampleLogs on each line.
Searching on mail ID format in log file is

  sender ->>>   from=\<sample_sender_id@example.com\> ,
  recipient ->>> to=\<sample_recipiend_id@example.com\>
  
Therefore you just need to input regular mail ID, example
sample_sender_id@example.com
Replace with true mail ID what you are actually looking for.

Result will come out with the whole line that is cooresponding with input by either sender mail ID or recipient mail ID which have been searching then matched in given file or log.
  
