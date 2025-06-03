# coding: utf-8

"""
EWK from the 2016 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


#########################################################################################
#########################           Drell-Yan           #################################
#########################################################################################
#########################               LO               ################################
#########################################################################################

cpn.add_dataset(
    name="dy_m10to50_madgraph",
    id=14341277,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34,  # 34-0
            n_events=22388550,
        ),
    ),
)

############################################################

# cpn.add_dataset(
#     name="dy_m50toinf_ht100to200_madgraph",
#     id=14248856,
#     processes=[procs.dy_m50toinf_ht100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=43,  # 43-0
#             n_events=8316351,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_ht1200to2500_madgraph",
#     id=14256439,
#     processes=[procs.dy_m50toinf_ht1200to2500],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=19,  # 19-0
#             n_events=1970857,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_ht200to400_madgraph",
#     id=14252965,
#     processes=[procs.dy_m50toinf_ht200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=26,  # 26-0
#             n_events=5653782,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_ht2500toinf_madgraph",
#     id=14255460,
#     processes=[procs.dy_m50toinf_ht2500toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=22,  # 22-0
#             n_events=696811,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_ht400to600_madgraph",
#     id=14276110,
#     processes=[procs.dy_m50toinf_ht400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=32,  # 32-0
#             n_events=2491416,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_ht600to800_madgraph",
#     id=14255233,
#     processes=[procs.dy_m50toinf_ht600to800],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=7,  # 7-0
#             n_events=2299853,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_ht70to100_madgraph",
#     id=14248562,
#     processes=[procs.dy_m50toinf_ht70to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=35,  # 35-0
#             n_events=5893910,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_ht800to1200_madgraph",
#     id=14251557,
#     processes=[procs.dy_m50toinf_ht800to1200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=36,  # 36-0
#             n_events=2393976,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=14521104,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCH3_13TeV-madgraphMLM-herwig7/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=18,  # 18-0
#             n_events=30069348,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=14521553,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCH3_13TeV-madgraphMLM-herwig7/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=58,  # 58-0
#             n_events=30069348,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=14653033,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCH3_13TeV-madgraphMLM-herwig7/RunIISummer20UL16NanoAODv9-20UL16JMENano_HerwigJetPartonBugFix_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=64,  # 64-0
#             n_events=30069348,
#         ),
#     ),
# )

cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14341272,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=61,  # 61-0
            n_events=82448537,
        ),
    ),
)

# cpn.add_dataset(
#     name="dy_m50toinf_madgraph",
#     id=14339903,
#     processes=[procs.dy_m50toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=130,  # 130-0
#             n_events=81877745,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_madgraph",
#     id=14702536,
#     processes=[procs.dy_m50toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-FSUL16_FSUL16_106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=7,  # 7-0
#             n_events=9998880,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_madgraph",
#     id=14229778,
#     processes=[procs.dy_m50toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-FlatPU0to75_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=10,  # 10-0
#             n_events=9915235,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="dy_m50toinf_madgraph",
#     id=14271013,
#     processes=[procs.dy_m50toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-FlatPU0to75_20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=21,  # 21-0
#             n_events=9885681,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=14355531,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_Zpt-100to200_BPSFilter_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=41,  # 41-0
#             n_events=4918136,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_madgraph",
#     id=14285555,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_Zpt-200toInf_BPSFilter_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=55,  # 55-0
#             n_events=734253,
#         ),
#     ),
# )



#########################################################################################
#########################           Drell-Yan           #################################
#########################################################################################
#########################               NLO               ################################
#########################################################################################

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14480799,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=25,  # 25-0
#             n_events=49267069,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14510060,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-500to700_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=19,  # 19-0
#             n_events=284416,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14300699,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=41,  # 41-0
#             n_events=71839442,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14386418,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=128,  # 128-0
#             n_events=73744428,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14266991,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_Pilot_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=7,  # 7-0
#             n_events=102477,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14463426,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-PUForTRK_106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=33,  # 33-0
#             n_events=101650,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14527642,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-PUForTRKv2_TRKv2_106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=25,  # 25-0
#             n_events=101079,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14845394,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-PilotMuonHits_106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=7,  # 7-0
#             n_events=10074,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14218851,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-Pilot_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=6,  # 6-0
#             n_events=102477,
#         ),
#     ),
# )

##############################################################################################################

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414428,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_1400_2300_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=6,  # 6-0
#             n_events=222311,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414819,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_200_400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=2480592,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414475,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_2300_3500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=2,  # 2-0
#             n_events=99246,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414639,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_3500_4500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=5,  # 5-0
#             n_events=50724,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414449,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_400_800_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=1,  # 1-0
#             n_events=249516,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14415072,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_4500_6000_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=25459,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414271,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_6000_Inf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=5,  # 5-0
#             n_events=25016,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414868,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_0J_MLL_800_1400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=251287,
#         ),
#     ),
# )

cpn.add_dataset(
    name="dy_0j_amcatnlo",
    id=14339807,
    processes=[procs.dy_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=60,  # 60-0
            n_events=73908089,
        ),
    ),
)

##################################################################################################################

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14415056,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_1400_2300_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=5,  # 5-0
#             n_events=247030,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14415476,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_200_400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=3,  # 3-0
#             n_events=1500285,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414157,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_2300_3500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=2,  # 2-0
#             n_events=104625,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410940,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_3500_4500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=10,  # 10-0
#             n_events=50137,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14415336,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_400_800_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=1,  # 1-0
#             n_events=249007,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14413924,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_4500_6000_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=3,  # 3-0
#             n_events=24990,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410867,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_6000_Inf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=5,  # 5-0
#             n_events=24979,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14415022,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_1J_MLL_800_1400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=3,  # 3-0
#             n_events=253960,
#         ),
#     ),
# )

cpn.add_dataset(
    name="dy_1j_amcatnlo",
    id=14340018,
    processes=[procs.dy_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=76,  # 76-0
            n_events=82259479,
        ),
    ),
)

##################################################################################################################


# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410976,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_1400_2300_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=13,  # 13-0
#             n_events=262757,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14418472,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_200_400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=2,  # 2-0
#             n_events=767699,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410977,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_2300_3500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=13,  # 13-0
#             n_events=97847,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410941,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_3500_4500_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=8,  # 8-0
#             n_events=50606,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14414744,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_400_800_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=261119,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410871,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_4500_6000_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=6,  # 6-0
#             n_events=24877,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410938,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_6000_Inf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=9,  # 9-0
#             n_events=25839,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14410982,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYJetsToLL_2J_MLL_800_1400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=10,  # 10-0
#             n_events=252970,
#         ),
#     ),
# )

cpn.add_dataset(
    name="dy_2j_amcatnlo",
    id=14234037,
    processes=[procs.dy_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=75,  # 75-0
            n_events=41816675,
        ),
    ),
)



##############################################################################################
######################      W boson production           #####################################
##############################################################################################

# inclusive

cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14231010,
    processes=[procs.w_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=68,  # 68-0
            n_events=80958227,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v2/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [],
            },
            n_files=796,  # 796-0
            n_events=80465376,
        ),
    ),
)


# ht binned

cpn.add_dataset(
    name="w_lnu_ht70to100_madgraph",
    id=14235559,
    processes=[procs.w_lnu_ht70to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=19439931,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v3/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [],
            },
            n_files=217,  # 217-0
            n_events=20470187,
        ),
    ),
)


cpn.add_dataset(
    name="w_lnu_ht100to200_madgraph",
    id=14235206,
    processes=[procs.w_lnu_ht100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=19753958,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v3/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [],
            },
            n_files=222,  # 222-0
            n_events=20519760,
        ),
    ),
)


cpn.add_dataset(
    name="w_lnu_ht200to400_madgraph",
    id=14230094,
    processes=[procs.w_lnu_ht200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=60,  # 60-0
            n_events=15067621,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v3/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [],
            },
            n_files=195,  # 195-0
            n_events=18394695,
        ),
    ),
)





cpn.add_dataset(
    name="w_lnu_ht400to600_madgraph",
    id=14232919,
    processes=[procs.w_lnu_ht400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,
            n_events=2115509,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext2-v3/NANOAODSIM"  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=89,
            n_events=2933634,
        ),
    ),
)


cpn.add_dataset(
    name="w_lnu_ht600to800_madgraph",
    id=14235199,
    processes=[procs.w_lnu_ht600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 113-0
            n_events=2251807,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext2-v3/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [],
            },
            n_files=113,  # 113-0
            n_events=4472075,
        ),
    ),
)


cpn.add_dataset(
    name="w_lnu_ht800to1200_madgraph",
    id=14229696,
    processes=[procs.w_lnu_ht800to1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=46,  # 46-0
            n_events=2132228,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext2-v3/NANOAODSIM",  # noqa
            ],
            aux={
                "broken_files": [],
            },
            n_files=134,  # 134-0
            n_events=4386343,
        )
    ),
)

cpn.add_dataset(
    name="w_lnu_ht1200to2500_madgraph",
    id=14271374,
    processes=[procs.w_lnu_ht1200to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=2090561,
        ),
        extension=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=124,  # 124-0
            n_events=3902685,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_ht2500toinf_madgraph",
    id=14238291,
    processes=[procs.w_lnu_ht2500toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=709514,
        ),
        extention=DatasetInfo(
            keys=[
                "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=709514,
        ),
    ),
)


##############################################################################################
######################    EWK (vector boson emissions)   #####################################
##############################################################################################

cpn.add_dataset(
    name="ewk_wm_lnu_m50toinf_madgraph",
    id=14230133,
    processes=[procs.ewk_wm_lnu_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=2202000,
        ),
    ),
)


cpn.add_dataset(
    name="ewk_wp_lnu_m50toinf_madgraph",
    id=14233017,
    processes=[procs.ewk_wp_lnu_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=2033000,
        ),
    ),
)


cpn.add_dataset(
    name="ewk_z_ll_m50toinf_madgraph",
    id=14229364,
    processes=[procs.ewk_z_ll_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,  # 10-0
            n_events=453000,
        ),
    ),
)


##############################################################################################
################################    Di-boson   ###############################################
##############################################################################################

cpn.add_dataset(
    name="zz_pythia8",
    id=14231227,
    processes=[procs.zz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=1151000,
        ),
    ),
)

# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_zqq_zll_amcatnlo",
    id=14297895,
    processes=[procs.zz_zqq_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=13740600,
        ),
    ),
)

# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_zll_znunu_powheg",
    id=14235549,
    processes=[procs.zz_zll_znunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=15928000,
        ),
    ),
)

# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=14345636,
    processes=[procs.zz_zll_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=99,  # 99-0
            n_events=52104000,
        ),
    ),
)


# WZ
cpn.add_dataset(
    name="wz_pythia8",
    id=14242203,
    processes=[procs.wz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=7584000,
        ),
    ),
)


# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="wz_wlnu_zll_amcatnlo",
    id=14234970,
    processes=[procs.wz_wlnu_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=31,  # 31-0
            n_events=10441724,
        ),
    ),
)


# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="wz_wqq_zll_amcatnlo",
    id=14283338,
    processes=[procs.wz_wqq_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=39,  # 39-0
            n_events=13526954,
        ),
    ),
)


# WW
cpn.add_dataset(
    name="ww_pythia8",
    id=14230242,
    processes=[procs.ww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=41,  # 41-0
            n_events=15821000,
        ),
    ),
)


cpn.add_dataset(
    name="ww_dl_powheg",
    id=14235253,
    processes=[procs.ww_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=2900000,
        ),
    ),
)



##############################################################################################
################################   Tri-boson   ###############################################
##############################################################################################


cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14229943,
    processes=[procs.zzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=4,  # 4-0
            n_events=72000,
        ),
        extension=DatasetInfo(
            keys=[
                "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=4534000,
        ),
    ),
)


cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14230874,
    processes=[procs.wzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=137000,
        ),
        extension=DatasetInfo(
            keys=[
                "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=6,  # 6-0
            n_events=4191000,
        ),
    ),
)


cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14230266,
    processes=[procs.wwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=67000,
        ),
        extension=DatasetInfo(
            keys=[
                "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=4595000,
        ),
    ),
)


cpn.add_dataset(
    name="www_amcatnlo",
    id=14230659,
    processes=[procs.www],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=69000,
        ),
        extension=DatasetInfo(
            keys=[
                "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=4159000,
        ),
    ),
)
