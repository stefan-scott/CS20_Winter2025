# Try-Except Demo
# To stop our programs from crashing...so much

my_list = [ 88  , 44  , "Twenty Two" ]
#           0      1         2              65

while True:
    try:
        index = int( input("Enter an index: ") ) #int() with non-num: Value Error
        chosen_num = my_list[index] #if index>2, IndexError (list out of range)
        print("Number: " + chosen_num) #TypeError. (if chosen_num is an int)
        break
#     except ValueError:
#         print("Value Error! Please enter a number")
#     except IndexError:
#         print("Index Error! Enter a number 0, 1, or 2")
#     except TypeError:
#         print("Type Error! Please select a string...")
    except:   #catch-all exception case
        print("Generic Error")