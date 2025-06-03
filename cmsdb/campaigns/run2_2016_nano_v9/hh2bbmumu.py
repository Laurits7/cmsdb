# coding: utf-8

"""
Higgs datasets for the 2016 data-taking campaign with datasets at NanoAOD tier in version 9.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn

# TODO: Check if the process is correct for the samples

cpn.add_dataset(
    name="hbb_hmm_kl0_kt1_powheg",
    id=14763275,
    processes=[procs.hbb_hmm_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHHToBBMuMuCHH0_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=44,  # 44-0
            n_events=250000,
        ),
    ),
)

cpn.add_dataset(
    name="hbb_hmm_kl0_kt1_p1wheg",
    id=14763230,
    processes=[procs.hbb_hmm_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHHToBBMuMuCHH1_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=250000,
        ),
    ),
)

cpn.add_dataset(
    name="hbb_hmm_kl2p45_kt1_powheg",
    id=14764013,
    processes=[procs.hbb_hmm_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHHToBBMuMuCHH2p45_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=91,  # 91-0
            n_events=238150,
        ),
    ),
)

cpn.add_dataset(
    name="hbb_hmm_kl5_kt1_powheg",
    id=14763061,
    processes=[procs.hbb_hmm_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHHToBBMuMuCHH5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=250000,
        ),
    ),
)
