import numpy as np
from Models import NeuralNetwork

# Load the default clf model

model=NeuralNetwork()


class Game():
    def __init__ (self, team1, team2):

        self.team1=team1
        self.team2=team2

    def predict(self, num_games):
        # output numpy array

        input_list=[]
        i=0
        while i < num_games:

            if (

                self.team1.initilized_from_players > 0 and
                self.team2.initilized_from_players == 0
            ):


                TwoPP=self.team1.simu_2PP_from_players() - self.team2.simu_2PP()
                ThreePP=self.team1.simu_3PP_from_players() - self.team2.simu_2PP()
                FTP=self.team1.simu_FTP_from_players() - self.team2.simu_FTP()
                OREBP=self.team1.simu_OREBP_from_players() - self.team2.simu_OREBP()
                DREBP=self.team1.simu_DREBP_from_players() - self.team2.simu_DREBP()
                ASSTP=self.team1.simu_ASSTP_from_players() - self.team2.simu_ASSTP()
                TOP=self.team1.simu_TOP_from_players() - self.team2.simu_TOP()
                STLP=self.team1.simu_STLP_from_players() - self.team2.simu_STLP()
                BLKP=self.team1.simu_BLKP_from_players() - self.team2.simu_BLKP()
                PF=self.team1.simu_PF_from_players() - self.team2.simu_PF()

            elif (
                    self.team1.initilized_from_players == 0 and
                    self.team1.initilized_from_players > 0
                ):

                TwoPP= self.team1.simu_2PP() - self.team2.simu_2PP_from_players()
                ThreePP= self.team1.simu_2PP() - self.team2.simu_3PP_from_players()
                FTP= self.team1.simu_FTP() - self.team2.simu_FTP_from_players()
                OREBP= self.team1.simu_OREBP() - self.team2.simu_OREBP_from_players()
                DREBP= self.team1.simu_DREBP() - self.team2.simu_DREBP_from_players()
                ASSTP= self.team1.simu_ASSTP() - self.team2.simu_ASSTP_from_players()
                TOP= self.team1.simu_TOP() - self.team2.simu_TOP_from_players()
                STLP= self.team1.simu_STLP() - self.team2.simu_STLP_from_players()
                BLKP= self.team1.simu_BLKP() - self.team2.simu_BLKP_from_players()
                PF= self.team1.simu_PF() - self.team2.simu_PF_from_players()


            elif (
                    self.team1.initilized_from_players == 0 and
                    self.team1.initilized_from_players == 0
                ):

                TwoPP= self.team1.simu_2PP() - self.team2.simu_2PP()
                ThreePP= self.team1.simu_3PP() - self.team2.simu_2PP()
                FTP= self.team1.simu_FTP() - self.team2.simu_FTP()
                OREBP= self.team1.simu_OREBP() - self.team2.simu_OREBP()
                DREBP= self.team1.simu_DREBP() - self.team2.simu_DREBP()
                ASSTP= self.team1.simu_ASSTP() - self.team2.simu_ASSTP()
                TOP= self.team1.simu_TOP() - self.team2.simu_TOP()
                STLP= self.team1.simu_STLP() - self.team2.simu_STLP()
                BLKP= self.team1.simu_BLKP() - self.team2.simu_BLKP()
                PF= self.team1.simu_PF() - self.team2.simu_PF()

            else:

                TwoPP= self.team1.simu_2PP_from_players() - self.team2.simu_2PP_from_players()
                ThreePP= self.team1.simu_3PP_from_players() - self.team2.simu_3PP_from_players()
                FTP= self.team1.simu_FTP_from_players()  - self.team2.simu_FTP_from_players()
                OREBP= self.team1.simu_OREBP_from_players() - self.team2.simu_OREBP_from_players()
                DREBP= self.team1.simu_DREBP_from_players() - self.team2.simu_DREBP_from_players()
                ASSTP= self.team1.simu_ASSTP_from_players() - self.team2.simu_ASSTP_from_players()
                TOP= self.team1.simu_TOP_from_players() - self.team2.simu_TOP_from_players()
                STLP= self.team1.simu_STLP_from_players()  - self.team2.simu_STLP_from_players()
                BLKP= self.team1.simu_BLKP_from_players()  - self.team2.simu_BLKP_from_players()
                PF= self.team1.simu_PF_from_players()  - self.team2.simu_PF_from_players()

            input=[TwoPP,ThreePP,FTP,OREBP,DREBP,ASSTP,TOP,STLP,BLKP,PF]
            input_list.append(input)

            i+=1

        X=np.array(input_list).reshape(-1, 10)
        result=model.predict(X)

        return result.reshape(-1,1)
