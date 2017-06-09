from spy_detail import spy, Spy, ChatMessage, friends#importing various class from spy_detail

from steganography.steganography import Steganography# for secret messaging througgh images

from Colors import bcolors #adding color into text

from datetime import datetime #use of current date and time value

STATUS_MESSAGES=['My name is khan','I am not a terrorist','Shaken, Not stirred']#predefined status messages

print 'Lets start'

question = 'Do u want to continue as '+spy.salutation+' '+spy.name+' '+' (Y/N)'
existing=raw_input(question)

def add_status():#function for adding a status

    updated_status_message = None

    #checking if the previous status was none or not
    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ") #selecting from previous status

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")# if no new status has been set


        if len(new_status_message) > 0: # adding new status
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))#selection of status messages


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message


def add_friend():

    new_friend = Spy('','',0,0.0)#adding a new friend on account a spy

    #taking friend's details
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

        #checking for authenticity of a friend
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


def select_a_friend():
    item_number = 0
        #function used for a selecting a particular  friend from a grouuup of friend
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#function for sending a secret messages

def send_message():
    #selecting a friend to whom u want to send the message
    friend_choice = select_a_friend()

    #name of the image
    original_image = raw_input("What is the name of the image?")
    #path of the image
    output_path = "output.jpg"
    #secret message
    text = raw_input("What do you want to say? ")

    # checking for the empty secret messages
    if len(text)>0:
        #make the message to secret
        Steganography.encode(original_image, output_path, text)

        new_chat = ChatMessage(text,True)
        #adding it to the chat message variable
        friends[friend_choice].chats.append(new_chat)

        print "Your secret message image is ready!"

    else:
        print "You have not enter the secret text"



def read_message():

    sender = select_a_friend()# select a spy whose message you want to acheive

    output_path = raw_input("What is the name of the file?")# file name which contains secret message

    text = Steganography.decode(output_path)

    if text.find("SOS"):    # if spy message contains some security problem it will show an alert before saving
        print "%s is in DANGER and needs your help !!!"%(friends[sender].name)

    if len(text)>100: #if spy message exceeds the limit of 100 then delete spy
        friends.remove(friends[sender])
        print "chat limmit exceeds the spy have been removed from spy group"
    else:    # adding the chat information into the list
        new_chat = ChatMessage(text,False)

        friends[sender].chats.append(new_chat)

        friends[sender].avg_word=len(text)

        print "Your secret message has been saved!"


def read_chat_history():

    read_for = select_a_friend()# select a friend whose message you want  to read

    print '\n6'

    for chat in friends[read_for].chats:#for repetitive chats
        if chat.sent_by_me:
            if chat.message.find("SOS"):#for any security alert
                print "You said: I was in DANGER !!!"
                #display the chat message and chat timing with color on it

            print '[%s] %s: %s' % (bcolors.BLUE +chat.time.strftime("%d %B %Y"),bcolors.RED+'You said:',bcolors.RESET+ chat.message)

        else:
            if chat.message.find("SOS"):
                print " %s said: I was in DANGER !!!"%(friends[read_for].name)
            print '[%s] %s said: %s' % (bcolors.BLUE+chat.time.strftime("%d %B %Y"),bcolors.RED+ friends[read_for].name,bcolors.RESET+ chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name #saving spy name with salutation


    if spy.age > 12 and spy.age < 50: #checking for authenticity of a spy


        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:#show repetive menu for multiple option till the spy don't exit from the program
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)#choice as per spy wish

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                    #condition and calling of function as per spy requests
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y":#if the spy already exist start chat directly
    start_chat(spy)
else:
    #taking the detail input of spy
    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'

        ##End Of the CODE