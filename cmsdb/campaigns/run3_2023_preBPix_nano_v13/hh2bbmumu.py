# coding: utf-8

"""
HH -> bbmumu datasets for the 2023 pre-BPix data-taking campaign
"""
from order import DatasetInfo
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v13 import campaign_run3_2023_preBPix_nano_v13 as cpn

#
# ggf, HH -> bbmumu
#

cpn.add_dataset(
    name="hh_ggf_hbb_hmm_kl1_kt1_powheg",
    id=14961118,
    processes=[procs.hh_ggf_hbb_hmm_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Mu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,  # 35-0
            n_events=331893,
        ),
    ),
)

cpn.add_dataset(
    name="hh_ggf_hbb_hmm_kl5_kt1_powheg",
    id=14965391,
    processes=[procs.hh_ggf_hbb_hmm_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Mu_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=76,  # 76-0
            n_events=332238,
        ),
    ),
)

cpn.add_dataset(
    name="hh_ggf_hbb_hmm_kl0_kt1_powheg",
    id=14962286,
    processes=[procs.hh_ggf_hbb_hmm_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Mu_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=65,  # 65-0
            n_events=332641,
        ),
    ),
)


#
# vbf, HH -> bbmumu
#

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14966363,
    processes=[procs.hh_vbf_hbb_hmm_kv1p74_k2v1p37_kl14p4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=333333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14966369,
    processes=[procs.hh_vbf_hbb_hmm_kvm1p6_k2v2p72_klm1p36],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=327333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14966279,
    processes=[procs.hh_vbf_hbb_hmm_kvm2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2,  # 2-0
            n_events=333333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14967037,
    processes=[procs.hh_vbf_hbb_hmm_kvm1p21_k2v1p94_klm0p94],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=329333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14968268,
    processes=[procs.hh_vbf_hbb_hmm_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=333333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kv1_k2v0_kl1_madgraph",
    id=14965432,
    processes=[procs.hh_vbf_hbb_hmm_kv1_k2v0_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=4,  # 4-0
            n_events=330333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kv1_k2v1_kl1_madgraph",
    id=14961071,
    processes=[procs.hh_vbf_hbb_hmm_kv1_k2v1_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=333333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14966850,
    processes=[procs.hh_vbf_hbb_hmm_kvm0p012_k2v0p03_kl10p2],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=333333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14966928,
    processes=[procs.hh_vbf_hbb_hmm_kvm1p83_k2v3p57_klm3p39],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=4,  # 4-0
            n_events=333333,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hmm_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14966996,
    processes=[procs.hh_vbf_hbb_hmm_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Mu_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=329333,
        ),
    ),
)
