import numpy as np
import Randomizers
import Player


class Team():

	def __init__(self, name):

		# All features range from 0 to 1, besides Personal Foul in integer.

		self.name=name

		self.TwoPointPercentage=0
		self.ThreePointPercentage=0
		self.FreeThrowPercentage=0
		self.OffensiveReboundPercentage=0
		self.DeffensiveReboundPercentage=0
		self.AssistPercentage=0
		self.TurnoverPercentage=0
		self.StealPercentage=0
		self.BlockPercentage=0
		self.PersonalFoul=0

		# internal handling

		self.player_list=[]
		self.initilized_from_players=0

		# initlization
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

	def team_up(self, player_list):

		self.player_list=player_list
		for i in player_list:
			self.initilized_from_players=self.initilized_from_players+1

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



	def simu_2PP_from_players(self):

		sum_2PP=0

		for player in self.player_list:
			sum_2PP = sum_2PP + player.simu_2PP()

		ave_2PP = sum_2PP / len(self.player_list)

		self.TwoPointPercentage=ave_2PP

		return self.TwoPointPercentage


	def simu_2PP(self):

		variate = Randomizers.simulate(self.TwoPP_bias, self.TwoPP_coefficient, self.TwoPP_distribution_type, self.TwoPP_paras)

		self.TwoPointPercentage=variate

		return self.TwoPointPercentage


	def simu_3PP_from_players(self):

		sum_3PP = 0

		for player in self.player_list:
			sum_3PP = sum_3PP + player.simu_3PP()

		ave_3PP = sum_3PP / len(self.player_list)

		self.ThreePointPercentage=ave_3PP

		return self.ThreePointPercentage


	def simu_3PP(self):

		variate = Randomizers.simulate(self.ThreePP_bias, self.ThreePP_coefficient, self.ThreePP_distribution_type, self.ThreePP_paras)

		self.ThreePointPercentage=variate

		return self.ThreePointPercentage


	def simu_FTP_from_players(self):

		sum_FPP = 0

		for player in self.player_list:
			sum_FPP = sum_FPP + player.simu_FTP()

		ave_FPP = sum_FPP / len(self.player_list)

		self.FreeThrowPercentage=ave_FPP

		return self.FreeThrowPercentage


	def simu_FTP(self):

		variate = Randomizers.simulate(self.FTP_bias, self.FTP_coefficient, self.FTP_distribution_type, self.FTP_paras)

		self.FreeThrowPercentage=variate

		return self.FreeThrowPercentage


	def simu_OREBP_from_players(self):

		sum_OREBP = 0

		for player in self.player_list:
			sum_OREBP = sum_OREBP + player.simu_OREBP()

		ave_OREBP = sum_OREBP / len(self.player_list)

		self.OffensiveReboundPercentage=ave_OREBP

		return self.OffensiveReboundPercentage


	def simu_OREBP(self):

		variate = Randomizers.simulate(self.OREBP_bias, self.OREBP_coefficient, self.OREBP_distribution_type, self.OREBP_paras)

		self.OffensiveReboundPercentage=variate

		return self.OffensiveReboundPercentage


	def simu_DREBP_from_players(self):

		sum_DREBP = 0

		for player in self.player_list:
			sum_DREBP = sum_DREBP + player.simu_DREBP()

		ave_DREBP = sum_DREBP / len(self.player_list)

		self.DeffensiveReboundPercentage=ave_DREBP

		return self.DeffensiveReboundPercentage


	def simu_DREBP(self):

		variate = Randomizers.simulate(self.DREBP_bias, self.DREBP_coefficient, self.DREBP_distribution_type, self.DREBP_paras)

		self.DeffensiveReboundPercentage=variate

		return self.DeffensiveReboundPercentage


	def simu_ASSTP_from_players(self):

		sum_ASSTP = 0

		for player in self.player_list:
			sum_ASSTP = sum_ASSTP + player.simu_ASSTP()

		ave_ASSTP = sum_ASSTP / len(self.player_list)

		self.AssistPercentage=ave_ASSTP

		return self.AssistPercentage


	def simu_ASSTP(self):

		variate = Randomizers.simulate(self.ASSTP_bias, self.ASSTP_coefficient, self.ASSTP_distribution_type, self.ASSTP_paras)

		self.AssistPercentage=variate

		return self.AssistPercentage


	def simu_TOP_from_players(self):

		sum_TOP = 0

		for player in self.player_list:
			sum_TOP = sum_TOP + player.simu_TOP()

		ave_TOP = sum_TOP / len(self.player_list)

		self.TurnoverPercentage=ave_TOP

		return self.TurnoverPercentage


	def simu_TOP(self):

		variate = Randomizers.simulate(self.TOP_bias, self.TOP_coefficient, self.TOP_distribution_type, self.TOP_paras)

		self.TurnoverPercentage=variate

		return self.TurnoverPercentage


	def simu_STLP_from_players(self):

		sum_STLP = 0

		for player in self.player_list:
			sum_STLP = sum_STLP + player.simu_STLP()

		ave_STLP = sum_STLP / len(self.player_list)

		self.StealPercentage=ave_STLP

		return self.StealPercentage


	def simu_STLP(self):

		variate = Randomizers.simulate(self.STLP_bias, self.STLP_coefficient, self.STLP_distribution_type, self.STLP_paras)

		self.StealPercentage=variate

		return self.StealPercentage


	def simu_BLKP_from_players(self):

		sum_BLKP = 0

		for player in self.player_list:
			sum_BLKP = sum_BLKP + player.simu_BLKP()

		ave_BLKP = sum_BLKP / len(self.player_list)

		self.BlockPercentage=ave_BLKP

		return self.BlockPercentage


	def simu_BLKP(self):

		variate = Randomizers.simulate(self.BLKP_bias, self.BLKP_coefficient, self.BLKP_distribution_type, self.BLKP_paras)

		self.BlockPercentage=variate

		return self.BlockPercentage


	def simu_PF_from_players(self):

		sum_PF=0

		for player in self.player_list:
			sum_PF = sum_PF + player.simu_PF()

		self.PersonalFoul=sum_PF

		return self.PersonalFoul


	def simu_PF(self):

		variate = Randomizers.simulate(self.PF_bias, self.PF_coefficient, self.PF_distribution_type, self.PF_paras)

		self.PersonalFoul=variate

		return self.PersonalFoul
