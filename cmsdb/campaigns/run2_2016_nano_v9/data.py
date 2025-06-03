# coding: utf-8

"""
CMS datasets from the 2016 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


#########################################################################################
#########################           DoubleEG           ##################################
#########################################################################################

# # Missing Run2016C, Run2016D, Run2016E now

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345102,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v3/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=67,  # 67-0
#             n_events=143073268,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14233080,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=5,  # 5-0
#             n_events=4360689,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14245425,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=47,  # 47-0
#             n_events=78797031,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14242917,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=86,  # 86-0
#             n_events=85388673,
#         ),
#     ),
# )


#########################################################################################
#########################           SingleElectron           ############################
#########################################################################################

# Missing Run2016B, Run2016C, Run2016D, Run2016E

cpn.add_dataset(
    name="data_e_f",
    id=14230145,
    processes=[procs.data_e],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "F"
            },
            n_files=5,  # 5-0
            n_events=8858206,
        ),
    ),
    aux={,
        "era": "F"
    },
)

cpn.add_dataset(
    name="data_e_g",
    id=14239294,
    processes=[procs.data_e],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "G"
            },
            n_files=71,  # 71-0
            n_events=153363109,
        ),
    ),
    aux={,
        "era": "G"
    },
)

cpn.add_dataset(
    name="data_e_h",
    id=14227078,
    processes=[procs.data_e],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": []
            },
            n_files=80,  # 80-0
            n_events=129021893,
        ),
    ),
    aux={,
        "era": "H"
    },
)



#########################################################################################
#########################           MuonEG           ####################################
#########################################################################################

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345261,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/MuonEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=1,  # 1-0
#             n_events=225271,
#         ),
#     ),
# )

cpn.add_dataset(
    name="data_muoneg_b",
    id=14345347,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=32727796,
        ),
    ),
    aux={,
        "era": "B"
    },
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=14345314,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=15405678,
        ),
    ),
    aux={,
        "era": "C"
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=14345278,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=23482352,
        ),
    ),
    aux={,
        "era": "D"
    },
)

cpn.add_dataset(
    name="data_muoneg_e",
    id=14344897,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=22519303,
        ),
    ),
    aux={,
        "era": "E"
    },
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=14345697,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=14100826,
        ),
    ),
    aux={,
        "era": "F"
    },
)

# cpn.add_dataset(
#     name="data_muoneg_f",
#     id=14227154,
#     processes=[procs.data_muoneg],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/MuonEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=3,  # 3-0
#             n_events=1901339,
#         ),
#     ),
#     aux={,
#         "era": "F"
#     },
# )

cpn.add_dataset(
    name="data_muoneg_g",
    id=14227077,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=29,  # 29-0
            n_events=33854612,
        ),
    ),
    aux={,
        "era": "G"
    },
)

cpn.add_dataset(
    name="data_muoneg_h",
    id=14227095,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=29236516,
        ),
    ),
    aux={,
        "era": "H"
    },
)


#########################################################################################
#########################           DoubleMuon           ################################
#########################################################################################


# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345322,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=3,  # 3-0
#             n_events=4199947,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345305,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=39,  # 39-0
#             n_events=82535526,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345330,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=16,  # 16-0
#             n_events=27934629,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345415,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=22,  # 22-0
#             n_events=33861745,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345210,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=19,  # 19-0
#             n_events=28246946,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14345031,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=10,  # 10-0
#             n_events=17900759,
#         ),
#     ),
# )

# # cpn.add_dataset(
# #     name="PLACEHOLDER",
# #     id=14232792,
# #     processes=[procs.PLACEHOLDER],
# #     info=dict(
# #         nominal=DatasetInfo(
# #             keys=[
# #                 "/DoubleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
# #             ],
# #             aux={
# #                 "broken_files": [],
# #             },
# #             n_files=1,  # 1-0
# #             n_events=2429162,
# #         ),
# #     ),
# # )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14258273,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=29,  # 29-0
#             n_events=45235604,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="PLACEHOLDER",
#     id=14256348,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DoubleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=28,  # 28-0
#             n_events=48912812,
#         ),
#     ),
# )

#########################################################################################
#########################           SingleMuon           ################################
#########################################################################################

# cpn.add_dataset(
#     name="data_muon_b",
#     id=14345036,
#     processes=[procs.data_muon],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=2,  # 2-0
#             n_events=2789243,
#         ),
#     ),
#     aux={,
#             "era": "B"
#         },
# )

cpn.add_dataset(
    name="data_mu_b",
    id=14345159,
    processes=[procs.data_mu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=70,  # 70-0
            n_events=158145722,
        ),
    ),
    aux={,
        "era": "B"
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=14345260,
    processes=[procs.data_mu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=67441308,
        ),
    ),
    aux={,
        "era": "C"
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14345352,
    processes=[procs.data_mu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=40,  # 40-0
            n_events=98017996,
        ),
    ),
    aux={,
        "era": "D"
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=14345735,
    processes=[procs.data_mu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=47,  # 47-0
            n_events=90984718,
        ),
    ),
    aux={,
        "era": "E"
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14345750,
    processes=[procs.data_mu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=43,  # 43-0
            n_events=57465359,
        ),
    ),
    aux={,
        "era": "F"
    },
)

# cpn.add_dataset(
#     name="data_mu_f",
#     id=14233029,
#     processes=[procs.data_mu],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=5,  # 5-0
#             n_events=8024195,
#         ),
#     ),
#     aux={,
#         "era": "F"
#     },
# )

cpn.add_dataset(
    name="data_mu_g",
    id=14227079,
    processes=[procs.data_mu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=70,  # 70-0
            n_events=149916849,
        ),
    ),
    aux={,
        "era": "H"
    },
)

cpn.add_dataset(
    name="data_mu_h",
    id=14227072,
    processes=[procs.data_mu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=82,  # 82-0
            n_events=174035164,
        ),
    ),
    aux={,
        "era": "H"
    },
)
