# coding: utf-8

"""
Higgs datasets for the 2016 data-taking campaign with datasets at NanoAOD tier in version 9.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=14283700,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=40,  # 40-0
            n_events=6439000,
        ),
    ),
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14317361,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToZZTo4L_M125_CP5TuneDown_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=9,  # 9-0
#             n_events=499998,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14327757,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToZZTo4L_M125_CP5TuneDown_13TeV_powheg2_minloHJJ_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=21,  # 21-0
#             n_events=1000000,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14317566,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToZZTo4L_M125_CP5TuneUp_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=11,  # 11-0
#             n_events=500000,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14370211,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToZZTo4L_M125_CP5TuneUp_13TeV_powheg2_minloHJJ_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=13,  # 13-0
#             n_events=999654,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14273782,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=8,  # 8-0
#             n_events=1000000,
#         ),
#     ),
# )

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14369580,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_minloHJJ_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=29,  # 29-0
            n_events=2994165,
        ),
    ),
)


########################################################################

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14276367,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToGG_M125_13TeV-sherpa/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=7,  # 7-0
#             n_events=964000,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=15112534,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToGG_M125_13TeV-sherpa/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=22,  # 22-0
#             n_events=597162,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14288207,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToGG_M125_TuneCP5Down_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=2,  # 2-0
#             n_events=885633,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14280023,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToGG_M125_TuneCP5Up_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=986010,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14288854,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=2042046,
#         ),
#     ),
# )

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15230351,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=61,  # 61-0
            n_events=7819095,
        ),
    ),
)


#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14315588,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToZZTo2L2Q_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=1000000,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14352086,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToBB_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=228000,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14616338,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1,  # 1-0
            n_events=500000,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14645470,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHToMuMu_M125_TuneCP5_withDipoleRecoil_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1,  # 1-0
            n_events=943000,
        ),
    ),
)

# #############################################

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14327699,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBF_HToZZTo4L_M125_CP5TuneDown_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=7,  # 7-0
#             n_events=495000,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14334575,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBF_HToZZTo4L_M125_CP5TuneUp_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=5,  # 5-0
#             n_events=486000,
#         ),
#     ),
# )

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14286118,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=498000,
        ),
    ),
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14337122,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBF_HToZZTo4L_M125_TuneCP5_withDipoleRecoil_13TeV-powheg2-jhugenv7011-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=15,  # 15-0
#             n_events=494000,
#         ),
#     ),
# )


#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14231660,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34,  # 34-0
            n_events=2987000,
        ),
    ),
)


#############################################

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14411109,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToBB_M-125_TuneCH3_13TeV-powheg-herwig/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=29,  # 29-0
#             n_events=3982131,
#         ),
#     ),
# )

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14276385,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=6,  # 6-0
            n_events=3514000,
        ),
    ),
)

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14265940,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToBB_M-125_dipoleRecoilOn_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=10,  # 10-0
#             n_events=3448742,
#         ),
#     ),
# )



#############################################

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14452120,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToGG_M125_TuneCP5Down_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=4000000,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_amcatnlo",
#     id=14434776,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToGG_M125_TuneCP5Up_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=4,  # 4-0
#             n_events=3991000,
#         ),
#     ),
# )

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=14316292,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHToGG_M125_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=62,  # 62-0
            n_events=3993140,
        ),
    ),
)

#############################################

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14560659,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToWWTo2L2Nu_M-125_CPS_NNPDF31_TuneCP5_withDipoleRecoil_13TeV-powheg-jhugen735-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=1,  # 1-0
#             n_events=246332,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14364308,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToWWTo2L2Nu_M-125_TuneCP5Down_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=28,  # 28-0
#             n_events=2861000,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",
#     id=14352205,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToWWTo2L2Nu_M-125_TuneCP5Up_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=15,  # 15-0
#             n_events=2899000,
#         ),
#     ),
# )

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14260716,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=38,  # 38-0
            n_events=2893000,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_madgraph",
    id=14280775,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/THQ_ctcvcp_4f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=77,  # 77-0
            n_events=14939986,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_madgraph",
    id=14353078,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/THW_ctcvcp_5f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,  # 35-0
            n_events=7484000,
        ),
    ),
)


#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14592723,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1,  # 1-0
            n_events=300000,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14592788,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1,  # 1-0
            n_events=300000,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14594064,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ttHToMuMu_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2,  # 2-0
            n_events=499068,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=14235005,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=4941250,
        ),
    ),
)


#############################################

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=14235190,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=5231575,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14618571,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHToMuMu_M125_CP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1,  # 1-0
            n_events=496320,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14265972,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=6,  # 6-0
            n_events=2419675,
        ),
    ),
)

#############################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14352989,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=2209078,
        ),
    ),
)
