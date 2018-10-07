#!/usr/bin/env python
# coding: utf-8

# Write Main Code Here
import re
#senderMail = 'bizdeissnsduizet@aol.jp'
#recipientMail = 'mtt.mht@mptmail.net.mm'
print('Type input FILE name exactly')
fileName = input()

# Define function to search cooresponding sender and recipient in the line
def allSearch(senderMail , recipientMail):
    i,j,k = 0,0,0
    with open(fileName) as f:
        for line in f:
            i += 1
            if senderMail is not None and recipientMail is '':  # Check input value of Sender is not None
                sender_match = re.search(r"from\=\<"+senderMail+">", line) # Search from=<xxxx@aaa.bb.cc>
                #
                recipient_match = False
            elif senderMail is '' and recipientMail is not None: # Check input value of Recipient is not None
                recipient_match = re.search(r"to\=\<"+recipientMail+">", line)  # Search to=<xxxx@aaa.bb.cc>
                sender_match = False
            else:
                sender_match = re.search(r"from\=\<"+senderMail+">", line)
                recipient_match = re.search(r"to\=\<"+recipientMail+">", line) 
# Boolean base defined to parse data                
            if sender_match and recipient_match:   # Find Sender and Recipient mail matching in the line
                sender_match = sender_match.group()
                sender_match = re.sub(r"^from\=\<", "", sender_match) # Eliminate 'from=<' in string
                sender_match = re.sub(r"\>$", "", sender_match)   # Eliminate '>' from in string
                sender_condition = True
           ###################################
                recipient_match = recipient_match.group()
                recipient_match = re.sub(r"^to\=\<", "", recipient_match) # Eliminate 'to=<' in string
                recipient_match = re.sub(r"\>$", "", recipient_match)   # Eliminate '>' in string
                recipient_condition = True
            elif sender_match is not None  and recipient_match == False: # Find Sender mail matching in the line
                #print(sender_match)
                sender_match = sender_match.group()
                sender_match = re.sub(r"^from\=\<", "", sender_match)
                sender_match = re.sub(r"\>$", "", sender_match)
                sender_condition = True
                recipient_condition = False
            elif sender_match == False and recipient_match is not None:  # Find Recipient mail matching in the line
                recipient_match = recipient_match.group()
                recipient_match = re.sub(r"^to\=\<", "", recipient_match)
                recipient_match = re.sub(r"\>$", "", recipient_match)
                recipient_condition = True
                sender_condition = False
            else:
                sender_condition = False
                recipient_condition = False
                k +=1   #Count unmatching records
                continue

            if sender_condition and recipient_condition:  # Print the line that contain the state of Sender and Recipient are matching in True.
                j += 1  #Initialize first row number
                print('-----> Matching with given sender and recipient ID <------')
                print('No : ' + str(j)+ ', Line : ' + str(i))
                print('-----------------------------')
                print(line)
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

            elif sender_condition == True and recipient_condition == False:  # Print the line that contain only the state of Sender is True.
                j += 1  #Initialize first row number
                print('-----> Matching with given sender ID <------')
                print('No : ' + str(j)+ ', Line : ' + str(i))
                print('-----------------------------')
                print(line)
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
            elif sender_condition == False and recipient_condition == True:  # Print the line that contain only the state of Recipient is True.
                j += 1  #Initialize first row number
                print('-----> Matching with given recipient ID <------')
                print('No : ' + str(j)+ ', Line : ' + str(i))
                print('-----------------------------')
                print(line)
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')      
                    
    if j:
        print('Number of total unmatched records found ' + str(k) + ' out of ' +str(i))
                
    else:
        print('Searching at total lines '+str(k)+' andd no matching was found!')
            
def askFromTo():
        print('Type Sender mail (from) or Press enter to next search (to) : ')
        senderMail = input()
        if senderMail == '':
            print('Type Recipient mail (to) or Press m go back menu : ')
            recipientMail = input()
            if recipientMail == 'm':
                #Go back menu
                askFromTo()
            elif recipientMail == '':
                print('You didn\' input anything, program EXIT')
                exit
            else:
                #Called only Recipient Function()
                allSearch(senderMail,recipientMail)
        else:
            print('Type Recipient mail (to) or Press enter to start searching only (from) or Press m go back menu : ')
            recipientMail = input()
            if recipientMail == '':
                #Called only Sender Function()
                allSearch(senderMail,recipientMail)
            elif recipientMail == 'm':
                askFromTo()
            else:
                #Called To and From Function()
                allSearch(senderMail,recipientMail)
  
askFromTo()                  
