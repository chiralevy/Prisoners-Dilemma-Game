"""
Chira Levy
CS051P
Assignment10
11/19/18

A great deal of game theory explores how competing people decide when the consequences of their decisions depend of the actions of others.
In this program, I simulate a classic example of a game analyzed in game theory known as the prisoner's dilemma.
In the game, two criminals (here, you and someone else) are being interrogated and must either confess to a crime or keep quiet.
Whether you are freed or imprisoned is contingent upon the actions of the other criminal.
"""

from random import*
from time import*
import signal
import sys


class Dilemma:
    """
    In this class, I am creating the  methods that will comprise the characteristics of a suspect and
    the changes that he or she will undergo. This class allows me to create objects or "suspects" in my main
    method. These methods include: get_suspect, suspect_decision, change_cooperation, and bio.
    """

    def __init__(self, suspect, cooperation=0, decision=""):
        """
        This constructor initializes the criminal's attributes: suspect(their name), cooperation, and their decision.
        :param suspect: This is the name of the suspect (type:str)
        :param cooperation: This is the suspect's level of cooperation, their likelihood to either confess or
         keep quiet(ranges from 0 to 10) (type: int)
        :param decision(type:str)
        :return: None
        """
        self.suspect = suspect
        self.decision = decision
        self.cooperation = cooperation

    def get_suspect(self):
        '''
        This accessor method returns the name of the suspect
        :return: This returns the name of the other suspect
        '''
        return self.suspect

    def suspect_decision(self):
        """
        This method uses the integer passed through the parameter of the object to determine whether the suspect
        confesses or keeps quiet. If the suspect's cooperation is greater than or equal to 5 they keep quiet; if
        it is below 5 they confess.

        :return: The initial decision of the other suspect (type: str)
        """

        if self.cooperation < 5:
            self.decision = 'Confess'

        if self.cooperation == 0:
            self.decision == 'Confess'

        if self.cooperation >= 5:
            self.decision = 'Keep Quiet'

        return self.decision

    def change_cooperation(self, decision):

        """
        This is a mutator method that changes the other suspect's cooperation in response to your decision.
        If they hear that you kept quiet, their cooperation will increase by two; if they hear that you confessed; their
        cooperation will decrease by two.

        :return: The new cooperation of the other suspect (type: int)
        """
        #if you Confessed(1), their cooperation will go down
        if decision == 'Confess':
            self.cooperation = self.cooperation - 2

        #If you kept quiet(0, their cooperation will go up
        if decision == 'Keep Quiet':
            self.cooperation = self.cooperation + 2

    def bio(self, cooperation):
        """
        This method assigns the suspect a quality based on their initial cooperation level. It ranges from
        sleazy to very loyal.

        :param cooperation: This is the suspect's initial cooperation level (type: int)
        :return: The character of a suspect based off of their initial cooperation (type: int)
        """

        character = 0
        for i in range(0, self.cooperation):
            character += 1

        if character in range(0, 4):
            return ("sleazy")
        if character in range(4, 7):
            return ("moderately trustworthy")
        if character in range(7, 11):
            return ("loyal")

    def __str__ (self):
        """
        When called this method gives the decision of the suspect
        :return: The suspect's decision (type: str)
        """

        return self.suspect + " chose to " + self.decision + ".\n"

def main():
    """
    My main method creates three different suspects (Spock, Robin, and Draco Malfoy) and their corresponding interrogation
    scenarios. Each round is divided into two parts, the first, the initial decisions, and the second, the decisions
    you and the other suspect make after finding out each other's initial decision. The second round is different
    because the suspect's cooperation will change depending on how you chose in the first round (up two if you kept quiet or down two if you confessed).
    Ultimately, if you and the suspect both keep quiet, you will both go to prison for one year. If you confess while the other suspect keeps quiet
    you're let free and they get ten years in prison--vice versa. If you both confess, you both get five years. ALl of the above methods are called.
    :return: None
    """

    print("___________.__               __________        .__                                /\          ________  .__.__                                 ")
    print("\__    ___/|  |__   ____     \______   \_______|__| __________   ____   __________)/ ______   \______ \ |__|  |   ____   _____   _____ _____   ")
    print("  |    |   |  |  \_/ __ \     |     ___/\_  __ \  |/  ___/  _ \ /    \_/ __ \_  __ \/  ___/    |    |  \|  |  | _/ __ \ /     \ /     \\__  \  ")
    print("  |    |   |   Y  \  ___/     |    |     |  | \/  |\___ (  <_> )   |  \  ___/|  | \/\___ \     |    `   \  |  |_\  ___/|  Y Y  \  Y Y  \/ __ \_")
    print("  |____|   |___|  /\___  >    |____|     |__|  |__/____  >____/|___|  /\___  >__|  /____  >   /_______  /__|____/\___  >__|_|  /__|_|  (____  /")
    print("                \/     \/                              \/           \/     \/           \/            \/             \/      \/      \/     \/ ")

    sleep(2)

    print("In this game, you are put in the shoes of one of two criminals being interrogated and must face a "
          "debilitating dilemma: confess or keep quiet.\nAs with all game theoretic dilemmas, your decisions "
          "are assessed against another's (here, the other criminal's) such that the outcome of your choices \n"
          "will depend critically on theirs. \n\nIf you both stay silent, "
          "you will both go to prison for one year. However, if you confess while the other suspect remains silent, "
          "\nyou're let free and they get ten years in prison--vice versa. While confessing might seem "
          "like the only way out, keep in mind that if you both \nhappen to confess, you will both face "
          "five years in prison. That is our dilemma...\n")

    input("Press Enter to continue...")
    print("\nShould you trust the other suspect to keep quiet?\n")
    sleep(2)
    print("Or do you shoot for freedom and risk the ten year sentence?\n")
    sleep(2)
    print("Is acting in your own self-interest wrong?\n")
    sleep(2)
    print("You decide.\n")
    sleep(2)

    print(("-" * 10) + "Scenario 1" + ("-" * 10))
    Spock = Dilemma("Spock", 8)
    print(("You and your long time friend, " + Spock.get_suspect() + ", find youselves in LAPD interrogation rooms for "
           "a crime you committed together 2 years ago.\nAlthough you are being interrogated separately, "
           "you know him to be " + Spock.bio(8) + " and have some intuition as "
           "to whether he will confess or keep quiet.\nWith this inkling, how will you act? Keep in mind he'll be "
           "informed of your decision and vice versa.\n"))

    while True:
        try:
            your_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
            break
        except ValueError:
            print("Try Again? 1 or 0.")

    Spock.suspect_decision()
    print(Spock)

    if your_decision == 1 and Spock.suspect_decision() == 'Confess':
        print("\nYou have both chosen too Confess, giving you both 5 years. You might want to think this over.\n")

        Spock.change_cooperation('Confess')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Spock.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Spock.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    if your_decision == 1 and Spock.suspect_decision() == 'Keep Quiet':
        print("You're free, but Spock might get ten years. Are you content with this outcome? Choose again.\n")

        Spock.change_cooperation('Confess')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Spock.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Spock.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    if your_decision == 0 and Spock.suspect_decision() == 'Confess':
        print("You might get 10 years. Are you content with this outcome? Choose again.\n")

        Spock.change_cooperation('Keep Quiet')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Spock.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Spock.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    if your_decision == 0 and Spock.suspect_decision() == 'Keep Quiet':

        print("You are both going to prison for one year. Are you content with this outcome? Choose again.\n")

        Spock.change_cooperation('Keep Quiet')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision ==1 and Spock.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Spock.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Confess':

            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Spock.suspect_decision() == 'Keep Quiet':

            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    print(("-" * 10) + "Scenario 2" + ("-" * 10))

    Robin = Dilemma("Robin", 5)
    print("Your past of vigilantism has finally caught up with you and your old partner in 'crime', "
          + Robin.get_suspect() + ". While you've known Robin to be a \n" + Robin.bio(5) + " sidekick, "
          "\n he's older now and, like you, thinks and acts independently. ""Also, he remembers that you flaked on him "
          "many times in the past, \nso he wont be so loyal if he finds out you confessed...\n")

    while True:
        try:
            your_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
            break
        except ValueError:
            print("Try Again? 1 or 0.")

    Robin.suspect_decision()
    print(Robin)

    if your_decision == 1 and Robin.suspect_decision() == 'Confess':
        print("You have both chosen to Confess, giving you both 5 years. You might want to think this over.\n")

        Robin.change_cooperation('Confess')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet.\n You are both going to prison for one year.\n")

    if your_decision == 1 and Robin.suspect_decision() == 'Keep Quiet':
        print("You're free, but Robin might get ten years. Are you content with this outcome? Choose again.\n")

        Robin.change_cooperation('Confess')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet.\n You are both going to prison for one year.\n")

    if your_decision == 0 and Robin.suspect_decision() == 'Confess':
        print("You might get 10 years. Are you content with this outcome? Choose again?\n")

        Robin.change_cooperation('Keep Quiet')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    if your_decision == 0 and Robin.suspect_decision() == 'Keep Quiet':

        print("You are both going to prison for one year. Are you content with this outcome? Choose again.\n")

        Robin.change_cooperation('Keep Quiet')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Robin.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Robin.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    print(("-" * 10) + "Scenario 3" + ("-" * 10))

    Draco = Dilemma("Draco Malfoy", 2)

    print("It was inevitable. " + Draco.get_suspect() + " spilled the beans about Slytherin's collusion in the "
          "Quidditch tounament(he paid you to sabotage Harry's broom) and now you are both \nin a serious interrogation"
          ". Draco's actions are almost a given (He's very " + Draco.bio(2) + ") and rumor has it that Azkaban "
          "will be the place of banishment.\nIt looks like Confession might be the only way...\n")

    while True:
        try:
            your_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
            break
        except ValueError:
            print("Try Again? 1 or 0.")

    Draco.suspect_decision()
    print(Draco)

    if your_decision == 1 and Draco.suspect_decision() == 'Confess':
        print("You have both chosen to Confess, giving you both 5 years. You might want to think this over.\n")

        Draco.change_cooperation('Confess')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    if your_decision == 1 and Draco.suspect_decision() == 'Keep Quiet':
        print("You're free, but Draco might get ten years. Are you content with this outcome? Choose again.\n")

        Draco.change_cooperation('Confess')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Confess':
            print("He Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    if your_decision == 0 and Draco.suspect_decision() == 'Confess':
        print("You might get 10 years. Are you content with this outcome? Choose again.\n")

        Draco.change_cooperation('Keep Quiet')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n")

    if your_decision == 0 and Draco.suspect_decision() == 'Keep Quiet':

        print("You are both going to prison for one year. Are you content with this outcome? Choose again.\n")

        Draco.change_cooperation('Keep Quiet')

        while True:
            try:
                your_new_decision = int(input("Type 1 to Confess and 0 to Keep Quiet.\n"))
                break
            except ValueError:
                print("Try Again? 1 or 0.")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Confess':
            print("You have both chosen to Confess. You are both getting 5 years.\n")

        if your_new_decision == 1 and Draco.suspect_decision() == 'Keep Quiet':
            print("They chose to stay quite. You are free, but they're going to prison for ten years.\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Confess':
            print("They Confessed. You are going to prison for 10 years.\n\n")

        if your_new_decision == 0 and Draco.suspect_decision() == 'Keep Quiet':
            print("You have both chosen to Keep Quiet. You are both going to prison for one year.\n\n")

    sleep(1)

    print("___________.__                   __     _____.___.                _____              __________.__                .__                ")
    print("\__    ___/|  |__ _____    ____ |  | __ \__  |   | ____  __ __  _/ ____\___________  \______   \  | _____  ___.__.|__| ____    ____  ")
    print("  |    |   |  |  \\\__  \  /    \|  |/ /  /   |   |/  _ \|  |  \ \   __\/  _ \_  __ \  |     ___/  | \__  \<   |  ||  |/    \  / ___\ ")
    print("  |    |   |   Y  \/ __ \|   |  \    <   \____   (  <_> )  |  /  |  | (  <_> )  | \/  |    |   |  |__/ __ \\\___  ||  |   |  \/ /_/  >")
    print("  |____|   |___|  (____  /___|  /__|_ \  / ______|\____/|____/   |__|  \____/|__|     |____|   |____(____  / ____||__|___|  /\___  / ")
    print("                \/     \/     \/     \/  \/                                                              \/\/             \//_____/  ")

    print("\nMore coming soon! Stay tuned...")

if __name__ == "__main__":
    main()
