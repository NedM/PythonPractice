name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt" #Default file name
handle = open(name) #Open files for read

target = "from "
senders = dict() #Dictionary Declaration

#Iterate through lines in the file
for line in handle:
    #Skip lines not starting with "From"
    if not line.lower().startswith(target): continue

    words = line.split()
    sender = words[1] #Sender is at index 1 in lines beginning with "From"
    senders[sender] = senders.get(sender, 0) + 1 #Use Dictionary 'Get value or default' function to count

mostTalkative = None
numEmails = None

for person,emails in senders.items():
    if numEmails is None or emails > numEmails:
        mostTalkative = person
        numEmails = emails

print mostTalkative, numEmails