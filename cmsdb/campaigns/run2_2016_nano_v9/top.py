# coding: utf-8

"""
Higgs datasets for the 2016 data-taking campaign with datasets at NanoAOD tier in version 9.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


##############################################################################################
#######################           ttbar           ############################################
##############################################################################################


cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14232826,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=49,  # 49-0
            n_events=43546000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14232860,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=138,  # 138-0
            n_events=144722000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14231933,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=146,  # 146-0
            n_events=107067000,
        ),
    ),
)


##############################################################################################
#######################         SingleTop         ############################################
##############################################################################################

cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14275700,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=3368375,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14238236,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=2491000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14238490,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=2554000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14258662,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,  # 35-0
            n_events=30609000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_powheg",
    id=14266078,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=86,  # 86-0
            n_events=63073000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=14341788,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=5471000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=14369560,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=5300000,
        ),
    ),
)


cpn.add_dataset(
    name="PLACEHOLDER_madgraph",
    id=14336383,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tWll_5f_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2,  # 2-0
            n_events=320000,
        ),
    ),
)
