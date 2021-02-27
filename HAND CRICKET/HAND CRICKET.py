from random import *
# TOSS
toss=choice(['heads','tails'])
#ININTIALISING INNINGS AS 1
innings=1
your_toss=input("enter heads or tails")
#Beginning of innings
if(innings==1):
   if(your_toss==toss):
     print('you have won the toss')
     choice_of=input('choose to bat or bowl')
     print("you have chosen to {}".format(choice_of))
# user is going to bat first
     if(choice_of.lower()=='bat'):
         print('you bat now')
         player_score = 0
         while (True):
             computer_input = randint(1, 6)
             user_input = int(input("choose a value between 1 and 6"))
             if(1<=user_input<=6):
               if (computer_input == user_input):
                 print("you are out")
                 print("your score is ", player_score)
                 break
               else:
                 player_score += user_input
                 print("computer bowled {}".format(computer_input))
                 print("you batted {}".format(user_input))
             else:
                 print('enter a number between 1 and 6')
         innings=2
         print("*************END OF FIRST INNINGS*************")
         print("now  computer will bat ")
         if(innings==2):
          computer_score = 0
          while (True):
             computer_input = randint(1, 6)
             user_input = int(input("choose a value between 1 and 6"))
             if (1 <= user_input <= 6):
               if (computer_input == user_input):
                 print("computer is out")
                 print("computer score is ", computer_score)
                 print('you win')
                 break
               else:
                 computer_score += computer_input
                 print("computer bated {}".format(computer_input))
                 print("you bowled {}".format(user_input))
                 if (computer_score > player_score):
                  print("the computer wins")
                  break
             else:
                 print('enter a number between 1 and 6')
# user has chosen to bowl first
     elif(choice_of.lower=='bowl'):
         computer_score = 0
         print('you bowl first')
         while (True):
             computer_input = randint(1, 6)
             user_input = int(input("choose a number between 1 and 6"))
             if (1 <= user_input <= 6):
               if (computer_input == user_input):
                 print("the computer is out")
                 print('the computer score is ', computer_score)
                 break
               else:
                 computer_score += computer_input
                 print("you have bowled {}".format(user_input))
                 print("the computer batted {}".format(computer_input))
             else:
                 print('enter a number between 1 and 6 ')
         print("*************END OF FIRST INNINGS*************")
         print('you bat now')
         innings = 2
         if(innings==2):
                 player_score = 0
                 while (True):
                     computer_input = randint(1, 6)
                     user_input = int(input("choose a value between 1 and 6"))
                     if (1 <= user_input <= 6):
                       if (computer_input == user_input):
                         print("you are out")
                         print("your score is ", player_score)
                         print('computer wins')
                         break
                       else:
                         player_score += user_input
                         print("computer bowled {}".format(computer_input))
                         print("you batted {}".format(user_input))
                         if (player_score > computer_score):
                          print('you win')
                          break
                     else:
                         print('enter number between 1 and 6')
   else:
       print("you have lost the toss")
       computer_choice=choice(['bat','bowl'])
       print("computer has chosen to {}".format(computer_choice))
# computer is batting first
       if(computer_choice=='bat'):
               computer_score = 0
               while (True):
                   computer_input = randint(1, 6)
                   user_input = int(input("choose a value between 1 and 6"))
                   if (1 <= user_input <= 6):
                     if (computer_input == user_input):
                       print("computer is out")
                       print("computer score is ", computer_score)
                       break
                     else:
                       computer_score += computer_input
                       print("computer bated {}".format(computer_input))
                       print("you bowled {}".format(user_input))
                   else:
                       print('enter a number between 1 and 6')
               innings=2
               print("*************END OF FIRST INNINGS*************")
               print('you bat now')
               if(innings==2):
                   player_score = 0
                   while (True):
                       computer_input = randint(1, 6)
                       user_input = int(input("choose a value between 1 and 6"))
                       if (1 <= user_input <= 6):
                         if (computer_input == user_input):
                           print("you are out")
                           print("your score is ", player_score)
                           print("the computer wins")
                           break
                         else:
                           player_score += user_input
                           print("computer bowled {}".format(computer_input))
                           print("you batted {}".format(user_input))
                           if (player_score > computer_score):
                            print('you win')
                            break
                       else:
                          print('enter a nummber between 1 and 6')

# computer has chosen to bowl
       elif(computer_choice=='bowl'):
           player_score = 0
           while (True):
               computer_input = randint(1, 6)
               user_input = int(input("choose a value between 1 and 6"))
               if (1 <= user_input <= 6):
                 if (computer_input == user_input):
                   print("you are out")
                   print("your score is ", player_score)
                   break
                 else:
                   player_score += user_input
                   print("computer bowled {}".format(computer_input))
                   print("you batted {}".format(user_input))
               else:
                   print('enter a value between 1 and 6')
           innings=2
           print("*************END OF FIRST INNINGS*************")
           print('computer bat now ')
           if(innings==2):
               computer_score = 0
               while (True):
                   computer_input = randint(1, 6)
                   user_input = int(input("choose a number between 1 and 6"))
                   if (1 <= user_input <= 6):
                     if (computer_input == user_input):
                       print("the computer is out")
                       print('the computer score is ', computer_score)
                       print('you win')
                       break
                     else:
                       computer_score += computer_input
                       print("you have bowled {}".format(user_input))
                       print("the computer batted {}".format(computer_input))
                       if (computer_score > player_score):
                        print('computer wins')
                        break
                   else:
                       print('enter a number between 1 and 6')
