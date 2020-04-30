import numpy as np
from Game import Game


class FirstRound():

    def __init__(self,

                group_A,
                group_B,
                group_C,
                group_D,
                group_E,
                group_F,
                group_G,
                group_H):

                self.team1=group_A[0]
                self.team2=group_A[1]
                self.team3=group_B[0]
                self.team4=group_B[1]
                self.team5=group_C[0]
                self.team6=group_C[1]
                self.team7=group_D[0]
                self.team8=group_D[1]
                self.team9=group_E[0]
                self.team10=group_E[1]
                self.team11=group_F[0]
                self.team12=group_F[1]
                self.team13=group_G[0]
                self.team14=group_G[1]
                self.team15=group_H[1]
                self.team16=group_H[1]


    def get_A_result(self, threshold=4):

        result=Game(self.team1, self.team2).predict(7)
        if sum(result) >= threshold:
            winner=self.team1
        else:
            winner=self.team2

            return winner


    def get_B_result(self, threshold=4):

        result=Game(self.team3, self.team4).predict(7)
        if sum(result) >= threshold:
            winner=self.team3
        else:
            winner=self.team4

            return winner


    def get_C_result(self, threshold=4):

        result=Game(self.team5, self.team6).predict(7)
        if sum(result) >= threshold:
            winner=self.team5
        else:
            winner=self.team6

            return winner


    def get_D_result(self, threshold=4):

        result=Game(self.team7, self.team8).predict(7)
        if sum(result) >= threshold:
            winner=self.team7
        else:
            winner=self.team8

            return winner


    def get_E_result(self, threshold=4):

        result=Game(self.team9, self.team10).predict(7)
        if sum(result) >= threshold:
            winner=self.team9
        else:
            winner=self.team10

            return winner


    def get_F_result(self, threshold=4):

        result=Game(self.team11, self.team12).predict(7)
        if sum(result) >= threshold:
            winner=self.team11
        else:
            winner=self.team12

            return winner


    def get_G_result(self, threshold=4):

        result=Game(self.team13, self.team14).predict(7)
        if sum(result) >= threshold:
            winner=self.team13
        else:
            winner=self.team14

            return winner


    def get_H_result(self, threshold=4):

        result=Game(self.team15, self.team16).predict(7)
        if sum(result) >= threshold:
            winner=self.team15
        else:
            winner=self.team16

            return winner

    def get_all_results(self, threshold=4):

        r1_A_winner=self.get_A_result()
        r1_B_winner=self.get_B_result()
        r1_C_winner=self.get_C_result()
        r1_D_winner=self.get_D_result()
        r1_E_winner=self.get_E_result()
        r1_F_winner=self.get_F_result()
        r1_G_winner=self.get_G_result()
        r1_H_winner=self.get_H_result()

        return r1_A_winner, r1_B_winner, r1_C_winner, r1_D_winner, r1_E_winner, r1_F_winner, r1_G_winner, r1_H_winner


class SecondRound():

    def __init__(self,

                group_A,
                group_B,
                group_C,
                group_D):

                self.team1=group_A[0]
                self.team2=group_A[1]
                self.team3=group_B[0]
                self.team4=group_B[1]
                self.team5=group_C[0]
                self.team6=group_C[1]
                self.team7=group_D[0]
                self.team8=group_D[1]


    def get_A_result(self, threshold=4):

        result=Game(self.team1, self.team2).predict(7)
        if sum(result) >= threshold:
            winner=self.team1
        else:
            winner=self.team2

            return winner


    def get_B_result(self, threshold=4):

        result=Game(self.team3, self.team4).predict(7)
        if sum(result) >= threshold:
            winner=self.team3
        else:
            winner=self.team4

            return winner


    def get_C_result(self, threshold=4):

        result=Game(self.team5, self.team6).predict(7)
        if sum(result) >= threshold:
            winner=self.team5
        else:
            winner=self.team6

            return winner


    def get_D_result(self, threshold=4):

        result=Game(self.team7, self.team8).predict(7)
        if sum(result) >= threshold:
            winner=self.team7
        else:
            winner=self.team8

            return winner


    def get_all_results(self, threshold=4):

        r1_A_winner=self.get_A_result()
        r1_B_winner=self.get_B_result()
        r1_C_winner=self.get_C_result()
        r1_D_winner=self.get_D_result()

        return r1_A_winner, r1_B_winner, r1_C_winner, r1_D_winner


class ThridRound():

    def __init__(self,

                group_A,
                group_B):

                self.team1=group_A[0]
                self.team2=group_A[1]
                self.team3=group_B[0]
                self.team4=group_B[1]


    def get_A_result(self, threshold=4):

        result=Game(self.team1, self.team2).predict(7)
        if sum(result) >= threshold:
            winner=self.team1
        else:
            winner=self.team2

            return winner


    def get_B_result(self, threshold=4):

        result=Game(self.team3, self.team4).predict(7)
        if sum(result) >= threshold:
            winner=self.team3
        else:
            winner=self.team4

            return winner

    def get_all_results(self, threshold=4):

        r1_A_winner=self.get_A_result()
        r1_B_winner=self.get_B_result()

        return r1_A_winner, r1_B_winner


class FinalRound():

    def __init__(self,

                group_final):

                self.team1=group_final[0]
                self.team2=group_final[1]


    def get_Final_results(self, threshold=4):

        result=Game(self.team1, self.team2).predict(7)
        if sum(result) >= threshold:
            champion=self.team1
        else:
            champion=self.team2

            return champion


class WholeTournament:

    def __init__(self):

        # Store Round 1 results
        self.r1_A=[]
        self.r1_B=[]
        self.r1_C=[]
        self.r1_D=[]
        self.r1_E=[]
        self.r1_F=[]
        self.r1_G=[]
        self.r1_H=[]

        # Store Round 2 results
        self.r2_A=[]
        self.r2_B=[]
        self.r2_C=[]
        self.r2_D=[]

        # Store Round 3 results
        self.r3_A=[]
        self.r3_B=[]

        # Store Final Round rresults
        self.r_final=[]


    def one_time_simu(self,

        group_A, group_B, group_C, group_D,
        group_E, group_F, group_G, group_H):

        FR=FirstRound(

        group_A, group_B, group_C, group_D,
        group_E, group_F, group_G, group_H

        )

        r2_team1,r2_team2,r2_team3,r2_team4,r2_team5,r2_team6,r2_team7,r2_team8 = FR.get_all_results()

        self.r1_A.append(str(r2_team1))
        self.r1_B.append(str(r2_team2))
        self.r1_C.append(str(r2_team3))
        self.r1_D.append(str(r2_team4))
        self.r1_E.append(str(r2_team5))
        self.r1_F.append(str(r2_team6))
        self.r1_G.append(str(r2_team7))
        self.r1_H.append(str(r2_team8))

        SR=SecondRound(

        (r2_team1,r2_team2),(r2_team3,r2_team4),(r2_team5,r2_team6),(r2_team7,r2_team8)

        )

        r3_team1,r3_team2,r3_team3, r3_team4 = SR.get_all_results()

        self.r2_A.append(str(r3_team1))
        self.r2_B.append(str(r3_team2))
        self.r2_C.append(str(r3_team3))
        self.r2_D.append(str(r3_team4))

        TR=ThridRound(

        (r2_team1,r2_team2),(r2_team3,r2_team4)

        )

        r4_team1,r4_team2=TR.get_all_results()

        self.r3_A.append(str(r4_team1))
        self.r3_B.append(str(r4_team2))

        FR=FinalRound(

        (r4_team1,r4_team2)

        )

        champion=FR.get_Final_results()
        self.r_final.append(str(champion))

        return champion
