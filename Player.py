
import numpy as np
import Randomizers

class Player():

    def __init__(self, name):

        self.name=name

        self.PlayerTwoPointPercentage=0
        self.PlayerThreePointPercentage=0
        self.PlayerFreeThrowPercentage=0
        self.PlayerOffensiveReboundPercentage=0
        self.PlayerDeffensiveReboundPercentage=0
        self.PlayerAssistPercentage=0
        self.PlayerTurnoverPercentage=0
        self.PlayerStealPercentage=0
        self.PlayerBlockPercentage=0
        self.PlayerPersonalFoul=0

        # initalization Parameters

        self.TwoPP_bias=0
        self.TwoPP_coefficient=0
        self.TwoPP_distribution_type='None'
        self.TwoPP_paras=[]

        self.ThreePP_bias=0
        self.ThreePP_coefficient=0
        self.ThreePP_distribution_type='None'
        self.ThreePP_paras=[]

        self.FTP_bias=0
        self.FTP_coefficient=0
        self.FTP_distribution_type='None'
        self.FTP_paras=[]

        self.OREBP_bias=0
        self.OREBP_coefficient=0
        self.OREBP_distribution_type='None'
        self.OREBP_paras=[]

        self.DREBP_bias=0
        self.DREBP_coefficient=0
        self.DREBP_distribution_type='None'
        self.DREBP_paras=[]

        self.ASSTP_bias=0
        self.ASSTP_coefficient=0
        self.ASSTP_distribution_type='None'
        self.ASSTP_paras=[]

        self.TOP_bias=0
        self.TOP_coefficient=0
        self.TOP_distribution_type='None'
        self.TOP_paras=[]

        self.STLP_bias=0
        self.STLP_coefficient=0
        self.STLP_distribution_type='None'
        self.STLP_paras=[]

        self.BLKP_bias=0
        self.BLKP_coefficient=0
        self.BLKP_distribution_type='None'
        self.BLKP_paras=[]

        self.PF_bias=0
        self.PF_coefficient=0
        self.PF_distribution_type='None'
        self.PF_paras=[]

    def __str__(self):

        return self.name

    # Initalization

    def init_2PP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.TwoPP_bias=bias
        self.TwoPP_coefficient=coefficient
        self.TwoPP_distribution_type=distribution_type
        self.TwoPP_paras=paras


    def init_3PP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.ThreePP_bias=bias
        self.ThreePP_coefficient=coefficient
        self.ThreePP_distribution_type=distribution_type
        self.ThreePP_paras=paras

    def init_FTP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.FTP_bias=bias
        self.FTP_coefficient=coefficient
        self.FTP_distribution_type=distribution_type
        self.FTP_paras=paras

    def init_OREBP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.OREBP_bias=bias
        self.OREBP_coefficient=coefficient
        self.OREBP_distribution_type=distribution_type
        self.OREBP_paras=paras


    def init_DREBP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.DREBP_bias=bias
        self.DREBP_coefficient=coefficient
        self.DREBP_distribution_type=distribution_type
        self.DREBP_paras=paras

    def init_ASSTP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.ASSTP_bias=bias
        self.ASSTP_coefficient=coefficient
        self.ASSTP_distribution_type=distribution_type
        self.ASSTP_paras=paras

    def init_TOP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.TOP_bias=bias
        self.TOP_coefficient=coefficient
        self.TOP_distribution_type=distribution_type
        self.TOP_paras=paras

    def init_STLP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.STLP_bias=bias
        self.STLP_coefficient=coefficient
        self.STLP_distribution_type=distribution_type
        self.STLP_paras=paras

    def init_BLKP(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.BLKP_bias=bias
        self.BLKP_coefficient=coefficient
        self.BLKP_distribution_type=distribution_type
        self.BLKP_paras=paras

    def init_PF(self, bias, coefficient=0, distribution_type='None', paras=[]):

        self.PF_bias=bias
        self.PF_coefficient=coefficient
        self.PF_distribution_type=distribution_type
        self.PF_paras=paras


    # simulation

    def simu_2PP(self):

        variate = Randomizers.simulate(self.TwoPP_bias, self.TwoPP_coefficient, self.TwoPP_distribution_type, self.TwoPP_paras)
        self.PlayerTwoPointPercentage=variate
        return self.PlayerTwoPointPercentage

    def simu_3PP(self):

        variate = Randomizers.simulate(self.ThreePP_bias, self.ThreePP_coefficient, self.ThreePP_distribution_type, self.ThreePP_paras)
        self.PlayerThreePointPercentage=variate
        return self.PlayerThreePointPercentage

    def simu_FTP(self):

        variate = Randomizers.simulate(self.FTP_bias, self.FTP_coefficient, self.FTP_distribution_type, self.FTP_paras)
        self.PlayerFreeThrowPercentage=variate
        return self.PlayerFreeThrowPercentage

    def simu_OREBP(self):

        variate = Randomizers.simulate(self.OREBP_bias, self.OREBP_coefficient, self.OREBP_distribution_type, self.OREBP_paras)
        self.PlayerOffensiveReboundPercentage=variate
        return self.PlayerOffensiveReboundPercentage

    def simu_DREBP(self):

        variate = Randomizers.simulate(self.DREBP_bias, self.DREBP_coefficient, self.DREBP_distribution_type, self.DREBP_paras)
        self.PlayerDeffensiveReboundPercentage=variate
        return self.PlayerDeffensiveReboundPercentage

    def simu_ASSTP(self):

        variate = Randomizers.simulate(self.ASSTP_bias, self.ASSTP_coefficient, self.ASSTP_distribution_type, self.ASSTP_paras)
        self.PlayerAssistPercentage=variate
        return self.PlayerAssistPercentage

    def simu_TOP(self):

        variate = Randomizers.simulate(self.TOP_bias, self.TOP_coefficient, self.TOP_distribution_type, self.TOP_paras)
        self.PlayerTurnoverPercentage=variate
        return self.PlayerTurnoverPercentage

    def simu_STLP(self):

        variate = Randomizers.simulate(self.STLP_bias, self.STLP_coefficient, self.STLP_distribution_type, self.STLP_paras)
        self.PlayerStealPercentage=variate
        return self.PlayerStealPercentage


    def simu_BLKP(self):

        variate = Randomizers.simulate(self.BLKP_bias, self.BLKP_coefficient, self.BLKP_distribution_type, self.BLKP_paras)
        self.PlayerBlockPercentage=variate
        return self.PlayerBlockPercentage

    def simu_PF(self):

        variate = Randomizers.simulate(self.PF_bias, self.PF_coefficient, self.PF_distribution_type, self.PF_paras)
        self.PlayerPersonalFoul=variate
        return self.PlayerPersonalFoul
