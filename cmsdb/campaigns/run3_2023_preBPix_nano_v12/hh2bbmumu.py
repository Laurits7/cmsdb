# coding: utf-8

"""
HH -> bbmumu datasets for the 2023 pre-BPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


# ggF

cpn.add_dataset(
    name="hh_ggf_hbb_hmm_kl2p45_kt1_powheg",
    id=14942536,
    processes=[procs.hh_ggf_hbb_hmm_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Mu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=85,  # 85-0
            n_events=358328,
        ),
    ),
)

# VBF
