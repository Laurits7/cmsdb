# coding: utf-8

"""
HH -> bbmumu process definitions.

IDs are assigned in the range 27100-27199 for hh_ggf and 28100-28199 for hh_vbf.
For radion ggf, the IDs are the range 29100-29199. As of 11.06.24, they go up to XXX.
For graviton ggf, the IDs are the range 30100-30199. As of 11.06.24, they go up to XXX.
For radion vbf, the IDs are the range 31100-31199. As of 11.06.24, they go up to XXX.
For graviton vbf, the IDs are the range 32100-32199. As of 11.06.24, they go up to XXX.
"""

__all__ = [
    "hh_ggf_hbb_hmm_kl1_kt1", "hh_ggf_hbb_hmm_kl0_kt1", "hh_ggf_hbb_hmm_kl0_kt1_c21",
    "hh_ggf_hbb_hmm_kl1_kt1_c20p10", "hh_ggf_hbb_hmm_kl1_kt1_c20p35", "hh_ggf_hbb_hmm_kl1_kt1_c23",
    "hh_ggf_hbb_hmm_kl1_kt1_c2m2", "hh_ggf_hbb_hmm_kl2p45_kt1", "hh_ggf_hbb_hmm_kl5_kt1",
    "hh_ggf_hbb_hmm_node1", "hh_ggf_hbb_hmm_node2", "hh_ggf_hbb_hmm_node3",
    "hh_ggf_hbb_hmm_node4", "hh_ggf_hbb_hmm_node5", "hh_ggf_hbb_hmm_node6",
    "hh_ggf_hbb_hmm_node7", "hh_ggf_hbb_hmm_node8", "hh_ggf_hbb_hmm_node9",
    "hh_ggf_hbb_hmm_node10", "hh_ggf_hbb_hmm_node11", "hh_ggf_hbb_hmm_node12",
    "radion_hh_ggf_hbb_hmm",
    "radion_hh_ggf_hbb_hmm_m250", "radion_hh_ggf_hbb_hmm_m260", "radion_hh_ggf_hbb_hmm_m270",
    "radion_hh_ggf_hbb_hmm_m280", "radion_hh_ggf_hbb_hmm_m300", "radion_hh_ggf_hbb_hmm_m320",
    "radion_hh_ggf_hbb_hmm_m350", "radion_hh_ggf_hbb_hmm_m400", "radion_hh_ggf_hbb_hmm_m450",
    "radion_hh_ggf_hbb_hmm_m500", "radion_hh_ggf_hbb_hmm_m550", "radion_hh_ggf_hbb_hmm_m600",
    "radion_hh_ggf_hbb_hmm_m650", "radion_hh_ggf_hbb_hmm_m700", "radion_hh_ggf_hbb_hmm_m750",
    "radion_hh_ggf_hbb_hmm_m800", "radion_hh_ggf_hbb_hmm_m850", "radion_hh_ggf_hbb_hmm_m900",
    "radion_hh_ggf_hbb_hmm_m1000", "radion_hh_ggf_hbb_hmm_m1100", "radion_hh_ggf_hbb_hmm_m1200",
    "radion_hh_ggf_hbb_hmm_m1250", "radion_hh_ggf_hbb_hmm_m1300", "radion_hh_ggf_hbb_hmm_m1400",
    "radion_hh_ggf_hbb_hmm_m1500", "radion_hh_ggf_hbb_hmm_m1600", "radion_hh_ggf_hbb_hmm_m1700",
    "radion_hh_ggf_hbb_hmm_m1750", "radion_hh_ggf_hbb_hmm_m1800", "radion_hh_ggf_hbb_hmm_m1900",
    "radion_hh_ggf_hbb_hmm_m2000", "radion_hh_ggf_hbb_hmm_m2200", "radion_hh_ggf_hbb_hmm_m2400",
    "radion_hh_ggf_hbb_hmm_m2500", "radion_hh_ggf_hbb_hmm_m2600", "radion_hh_ggf_hbb_hmm_m2800",
    "radion_hh_ggf_hbb_hmm_m3000", "radion_hh_ggf_hbb_hmm_m4000", "radion_hh_ggf_hbb_hmm_m5000",
    "graviton_hh_ggf_hbb_hmm",
    "graviton_hh_ggf_hbb_hmm_m250", "graviton_hh_ggf_hbb_hmm_m260",
    "graviton_hh_ggf_hbb_hmm_m270", "graviton_hh_ggf_hbb_hmm_m280",
    "graviton_hh_ggf_hbb_hmm_m300", "graviton_hh_ggf_hbb_hmm_m320",
    "graviton_hh_ggf_hbb_hmm_m350", "graviton_hh_ggf_hbb_hmm_m400",
    "graviton_hh_ggf_hbb_hmm_m450", "graviton_hh_ggf_hbb_hmm_m500",
    "graviton_hh_ggf_hbb_hmm_m550", "graviton_hh_ggf_hbb_hmm_m600",
    "graviton_hh_ggf_hbb_hmm_m650", "graviton_hh_ggf_hbb_hmm_m700",
    "graviton_hh_ggf_hbb_hmm_m750", "graviton_hh_ggf_hbb_hmm_m800",
    "graviton_hh_ggf_hbb_hmm_m850", "graviton_hh_ggf_hbb_hmm_m900",
    "graviton_hh_ggf_hbb_hmm_m1000", "graviton_hh_ggf_hbb_hmm_m1200",
    "graviton_hh_ggf_hbb_hmm_m1250", "graviton_hh_ggf_hbb_hmm_m1400",
    "graviton_hh_ggf_hbb_hmm_m1500", "graviton_hh_ggf_hbb_hmm_m1600",
    "graviton_hh_ggf_hbb_hmm_m1750", "graviton_hh_ggf_hbb_hmm_m1800",
    "graviton_hh_ggf_hbb_hmm_m2000", "graviton_hh_ggf_hbb_hmm_m2500",
    "graviton_hh_ggf_hbb_hmm_m3000", "graviton_hh_ggf_hbb_hmm_m4000",
    "graviton_hh_ggf_hbb_hmm_m5000",
    "hh_vbf_hbb_hmm_kv1_k2v1_kl1", "hh_vbf_hbb_hmm_kv1_k2v0_kl1", "hh_vbf_hbb_hmm_kv1_k2v1_kl2",
    "hh_vbf_hbb_hmm_kv1_k2v2_kl1", "hh_vbf_hbb_hmm_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hbb_hmm_kvm0p012_k2v0p03_kl10p2", "hh_vbf_hbb_hmm_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hbb_hmm_kvm0p962_k2v0p959_klm1p43", "hh_vbf_hbb_hmm_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hbb_hmm_kvm1p6_k2v2p72_klm1p36", "hh_vbf_hbb_hmm_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hbb_hmm_kvm2p12_k2v3p87_klm5p96",
    "radion_hh_vbf_hbb_hmm",
    "radion_hh_vbf_hbb_hmm_m250", "radion_hh_vbf_hbb_hmm_m260", "radion_hh_vbf_hbb_hmm_m270",
    "radion_hh_vbf_hbb_hmm_m280", "radion_hh_vbf_hbb_hmm_m300", "radion_hh_vbf_hbb_hmm_m320",
    "radion_hh_vbf_hbb_hmm_m350", "radion_hh_vbf_hbb_hmm_m400", "radion_hh_vbf_hbb_hmm_m450",
    "radion_hh_vbf_hbb_hmm_m500", "radion_hh_vbf_hbb_hmm_m550", "radion_hh_vbf_hbb_hmm_m600",
    "radion_hh_vbf_hbb_hmm_m650", "radion_hh_vbf_hbb_hmm_m700", "radion_hh_vbf_hbb_hmm_m750",
    "radion_hh_vbf_hbb_hmm_m800", "radion_hh_vbf_hbb_hmm_m850", "radion_hh_vbf_hbb_hmm_m900",
    "radion_hh_vbf_hbb_hmm_m1000", "radion_hh_vbf_hbb_hmm_m1250", "radion_hh_vbf_hbb_hmm_m1500",
    "radion_hh_vbf_hbb_hmm_m1750", "radion_hh_vbf_hbb_hmm_m2000", "radion_hh_vbf_hbb_hmm_m2500",
    "radion_hh_vbf_hbb_hmm_m3000",
    "graviton_hh_vbf_hbb_hmm",
    "graviton_hh_vbf_hbb_hmm_m250", "graviton_hh_vbf_hbb_hmm_m260",
    "graviton_hh_vbf_hbb_hmm_m270", "graviton_hh_vbf_hbb_hmm_m280",
    "graviton_hh_vbf_hbb_hmm_m300", "graviton_hh_vbf_hbb_hmm_m320",
    "graviton_hh_vbf_hbb_hmm_m350", "graviton_hh_vbf_hbb_hmm_m400",
    "graviton_hh_vbf_hbb_hmm_m450", "graviton_hh_vbf_hbb_hmm_m500",
    "graviton_hh_vbf_hbb_hmm_m550", "graviton_hh_vbf_hbb_hmm_m600",
    "graviton_hh_vbf_hbb_hmm_m650", "graviton_hh_vbf_hbb_hmm_m700",
    "graviton_hh_vbf_hbb_hmm_m750", "graviton_hh_vbf_hbb_hmm_m800",
    "graviton_hh_vbf_hbb_hmm_m850", "graviton_hh_vbf_hbb_hmm_m900",
    "graviton_hh_vbf_hbb_hmm_m1000", "graviton_hh_vbf_hbb_hmm_m1250",
    "graviton_hh_vbf_hbb_hmm_m1500", "graviton_hh_vbf_hbb_hmm_m1750",
    "graviton_hh_vbf_hbb_hmm_m2000", "graviton_hh_vbf_hbb_hmm_m2500",
    "graviton_hh_vbf_hbb_hmm_m3000",
]

import cmsdb.constants as const

from cmsdb.processes.hh import (
    hh_ggf, radion_hh_ggf, graviton_hh_ggf, hh_vbf, radion_hh_vbf, graviton_hh_vbf,
    hh_ggf_kl1_kt1, hh_ggf_kl0_kt1, hh_ggf_kl0_kt1_c21,
    hh_ggf_kl1_kt1_c20p10, hh_ggf_kl1_kt1_c20p35, hh_ggf_kl1_kt1_c23,
    hh_ggf_kl1_kt1_c2m2, hh_ggf_kl2p45_kt1, hh_ggf_kl5_kt1,
    hh_vbf_kv1_k2v1_kl1, hh_vbf_kv1_k2v0_kl1, hh_vbf_kv1_k2v1_kl2,
    hh_vbf_kv1_k2v2_kl1, hh_vbf_kv1p74_k2v1p37_kl14p4,
    hh_vbf_kvm0p012_k2v0p03_kl10p2, hh_vbf_kvm0p758_k2v1p44_klm19p3,
    hh_vbf_kvm0p962_k2v0p959_klm1p43, hh_vbf_kvm1p21_k2v1p94_klm0p94,
    hh_vbf_kvm1p6_k2v2p72_klm1p36, hh_vbf_kvm1p83_k2v3p57_klm3p39,
    hh_vbf_kvm2p12_k2v3p87_klm5p96,
)
from cmsdb.xsec_bsm_nodes import calculate_xsec_node
from cmsdb.util import multiply_xsecs


#
# ggF -> H -> HH
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hbb_hmm = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm",
    id=27100,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$",
)

hh_ggf_hbb_hmm_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hbb_hmm_kl1_kt1",
    id=27101,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_node1 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node1",
    id=27102,
    label=f"{hh_ggf_hbb_hmm.label} (node 1)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=1),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=1),
    },
)

hh_ggf_hbb_hmm_node2 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node2",
    id=27103,
    label=f"{hh_ggf_hbb_hmm.label} (node 2)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=2),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=2),
    },
)

hh_ggf_hbb_hmm_node3 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node3",
    id=27104,
    label=f"{hh_ggf_hbb_hmm.label} (node 3)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=3),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=3),
    },
)

hh_ggf_hbb_hmm_node4 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node4",
    id=27105,
    label=f"{hh_ggf_hbb_hmm.label} (node 4)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=4),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=4),
    },
)

hh_ggf_hbb_hmm_node5 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node5",
    id=27106,
    label=f"{hh_ggf_hbb_hmm.label} (node 5)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=5),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=5),
    },
)

hh_ggf_hbb_hmm_node6 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node6",
    id=27107,
    label=f"{hh_ggf_hbb_hmm.label} (node 6)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=6),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=6),
    },
)

hh_ggf_hbb_hmm_node7 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node7",
    id=27108,
    label=f"{hh_ggf_hbb_hmm.label} (node 7)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=7),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=7),
    },
)

hh_ggf_hbb_hmm_node8 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node8",
    id=27109,
    label=f"{hh_ggf_hbb_hmm.label} (node 8)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=8),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=8),
    },
)

hh_ggf_hbb_hmm_node9 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node9",
    id=27110,
    label=f"{hh_ggf_hbb_hmm.label} (node 9)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=9),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=9),
    },
)

hh_ggf_hbb_hmm_node10 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node10",
    id=27111,
    label=f"{hh_ggf_hbb_hmm.label} (node 10)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=10),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=10),
    },
)

hh_ggf_hbb_hmm_node11 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node11",
    id=27112,
    label=f"{hh_ggf_hbb_hmm.label} (node 11)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=11),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=11),
    },
)

hh_ggf_hbb_hmm_node12 = hh_ggf.add_process(
    name="hh_ggf_hbb_hmm_node12",
    id=27113,
    label=f"{hh_ggf_hbb_hmm.label} (node 12)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13), node_number=12),
        13.6: calculate_xsec_node(13.6, hh_ggf_hbb_hmm_kl1_kt1.get_xsec(13.6), node_number=12),
    },
)

hh_ggf_hbb_hmm_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hbb_hmm_kl0_kt1",
    id=27114,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_kl0_kt1_c21 = hh_ggf_kl0_kt1_c21.add_process(
    name="hh_ggf_hbb_hmm_kl0_kt1_c21",
    id=27115,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda} = 0$, $\kappa_t = 1, C_2 = 1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1_c21, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_kl1_kt1_c20p10 = hh_ggf_kl1_kt1_c20p10.add_process(
    name="hh_ggf_hbb_hmm_kl1_kt1_c20p10",
    id=27116,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = 0.1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1_c20p10, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_kl1_kt1_c20p35 = hh_ggf_kl1_kt1_c20p35.add_process(
    name="hh_ggf_hbb_hmm_kl1_kt1_c20p35",
    id=27117,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = 0.35$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1_c20p35, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_kl1_kt1_c23 = hh_ggf_kl1_kt1_c23.add_process(
    name="hh_ggf_hbb_hmm_kl1_kt1_c23",
    id=27118,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = 3$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1_c23, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_kl1_kt1_c2m2 = hh_ggf_kl1_kt1_c2m2.add_process(
    name="hh_ggf_hbb_hmm_kl1_kt1_c2m2",
    id=27119,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = -2$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1_c2m2, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hbb_hmm_kl2p45_kt1",
    id=27120,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda} = 2.45$, $\kappa_t = 1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.bbmm),
)

hh_ggf_hbb_hmm_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hbb_hmm_kl5_kt1",
    id=27121,
    label=r"$HH_{ggf} \rightarrow bb\mu\mu$ ($\kappa_{\lambda} = 5$, $\kappa_t = 1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.bbmm),
)


#
# ggF -> radion -> HH
#

radion_hh_ggf_hbb_hmm = radion_hh_ggf.add_process(
    name="radion_hh_ggf_hbb_hmm",
    id=29100,
    label=rf"{radion_hh_ggf.label} $\rightarrow bb\mu\mu$",
    xsecs=multiply_xsecs(radion_hh_ggf, const.br_hh.bbmm),
)

radion_hh_ggf_hbb_hmm_m250 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m250",
    id=29101,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m260 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m260",
    id=29102,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m270 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m270",
    id=29103,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m280 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m280",
    id=29104,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m300 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m300",
    id=29105,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m320 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m320",
    id=29106,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m350 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m350",
    id=29107,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m400 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m400",
    id=29108,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m450 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m450",
    id=29109,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m500 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m500",
    id=29110,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m550 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m550",
    id=29111,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m600 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m600",
    id=29112,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m650 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m650",
    id=29113,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m700 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m700",
    id=29114,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m750 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m750",
    id=29115,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m800 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m800",
    id=29116,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m850 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m850",
    id=29117,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m900 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m900",
    id=29118,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1000 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1000",
    id=29119,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1100 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1100",
    id=29120,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1200 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1200",
    id=29121,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1250 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1250",
    id=29122,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1300 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1300",
    id=29123,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1400 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1400",
    id=29124,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1500 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1500",
    id=29125,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1600 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1600",
    id=29126,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1700 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1700",
    id=29127,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1750 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1750",
    id=29128,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1800 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1800",
    id=29129,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m1900 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m1900",
    id=29130,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m2000 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m2000",
    id=29131,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m2200 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m2200",
    id=29132,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m2400 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m2400",
    id=29133,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m2500 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m2500",
    id=29134,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m2600 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m2600",
    id=29135,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m2800 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m2800",
    id=29136,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m3000 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m3000",
    id=29137,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m4000 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m4000",
    id=29138,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

radion_hh_ggf_hbb_hmm_m5000 = radion_hh_ggf_hbb_hmm.add_process(
    name="radion_hh_ggf_hbb_hmm_m5000",
    id=29139,
    xsecs=radion_hh_ggf_hbb_hmm.xsecs.copy(),
)

#
# ggF -> bulk graviton -> HH
#

graviton_hh_ggf_hbb_hmm = graviton_hh_ggf.add_process(
    name="graviton_hh_ggf_hbb_hmm",
    id=30100,
    label=rf"{graviton_hh_ggf.label} $\rightarrow bb\mu\mu$",
    xsecs=multiply_xsecs(graviton_hh_ggf, const.br_hh.bbmm),
)

graviton_hh_ggf_hbb_hmm_m250 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m250",
    id=30101,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m260 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m260",
    id=30102,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m270 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m270",
    id=30103,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m280 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m280",
    id=30104,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m300 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m300",
    id=30105,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m320 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m320",
    id=30106,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m350 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m350",
    id=30107,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m400 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m400",
    id=30108,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m450 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m450",
    id=30109,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m500 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m500",
    id=30110,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m550 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m550",
    id=30111,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m600 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m600",
    id=30112,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m650 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m650",
    id=30113,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m700 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m700",
    id=30114,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m750 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m750",
    id=30115,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m800 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m800",
    id=30116,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m850 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m850",
    id=30117,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m900 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m900",
    id=30118,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1000 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1000",
    id=30119,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1200 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1200",
    id=30120,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1250 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1250",
    id=30121,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1400 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1400",
    id=30122,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1500 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1500",
    id=30123,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1600 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1600",
    id=30124,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1750 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1750",
    id=30125,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m1800 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m1800",
    id=30126,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m2000 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m2000",
    id=30127,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m2500 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m2500",
    id=30128,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m3000 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m3000",
    id=30129,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m4000 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m4000",
    id=30130,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

graviton_hh_ggf_hbb_hmm_m5000 = graviton_hh_ggf_hbb_hmm.add_process(
    name="graviton_hh_ggf_hbb_hmm_m5000",
    id=30131,
    xsecs=graviton_hh_ggf_hbb_hmm.xsecs.copy(),
)

#
# vbf -> H -> HH
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hbb_hmm = hh_vbf.add_process(
    name="hh_vbf_hbb_hmm",
    id=28100,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$",
)

hh_vbf_hbb_hmm_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hbb_hmm_kv1_k2v1_kl1",
    id=28101,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ (SM)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hbb_hmm_kv1_k2v0_kl1",
    id=28102,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kv1_k2v1_kl2 = hh_vbf_kv1_k2v1_kl2.add_process(
    name="hh_vbf_hbb_hmm_kv1_k2v1_kl2",
    id=28103,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=2$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl2, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kv1_k2v2_kl1 = hh_vbf_kv1_k2v2_kl1.add_process(
    name="hh_vbf_hbb_hmm_kv1_k2v2_kl1",
    id=28104,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=1$, $\kappa_{2V}=2$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v2_kl1, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hbb_hmm_kv1p74_k2v1p37_kl14p4",
    id=28105,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hbb_hmm_kvm0p012_k2v0p03_kl10p2",
    id=28106,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hbb_hmm_kvm0p758_k2v1p44_klm19p3",
    id=28107,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hbb_hmm_kvm0p962_k2v0p959_klm1p43",
    id=28108,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hbb_hmm_kvm1p21_k2v1p94_klm0p94",
    id=28109,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hbb_hmm_kvm1p6_k2v2p72_klm1p36",
    id=28110,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hbb_hmm_kvm1p83_k2v3p57_klm3p39",
    id=28111,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.bbmm),
)

hh_vbf_hbb_hmm_kvm2p12_k2v3p87_klm5p96 = hh_vbf_kvm2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hbb_hmm_kvm2p12_k2v3p87_klm5p96",
    id=28112,
    label=r"$HH_{vbf} \rightarrow bb\mu\mu$ ($\kappa_{V}=-2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kvm2p12_k2v3p87_klm5p96, const.br_hh.bbmm),
)

#
# vbf -> radion -> HH
#

radion_hh_vbf_hbb_hmm = radion_hh_vbf.add_process(
    name="radion_hh_vbf_hbb_hmm",
    id=31100,
    label=rf"{radion_hh_vbf.label} $\rightarrow bb\mu\mu$",
    xsecs=multiply_xsecs(radion_hh_vbf, const.br_hh.bbmm),
)

radion_hh_vbf_hbb_hmm_m250 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m250",
    id=31101,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m260 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m260",
    id=31102,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m270 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m270",
    id=31103,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m280 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m280",
    id=31104,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m300 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m300",
    id=31105,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m320 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m320",
    id=31106,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m350 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m350",
    id=31107,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m400 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m400",
    id=31108,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m450 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m450",
    id=31109,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m500 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m500",
    id=31110,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m550 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m550",
    id=31111,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m600 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m600",
    id=31112,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m650 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m650",
    id=31113,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m700 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m700",
    id=31114,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m750 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m750",
    id=31115,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m800 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m800",
    id=31116,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m850 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m850",
    id=31117,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m900 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m900",
    id=31118,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m1000 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m1000",
    id=31119,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m1250 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m1250",
    id=31120,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m1500 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m1500",
    id=31121,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m1750 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m1750",
    id=31122,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m2000 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m2000",
    id=31123,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m2500 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m2500",
    id=31124,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)

radion_hh_vbf_hbb_hmm_m3000 = radion_hh_vbf_hbb_hmm.add_process(
    name="radion_hh_vbf_hbb_hmm_m3000",
    id=31125,
    xsecs=radion_hh_vbf_hbb_hmm.xsecs.copy(),
)


#
# vbf -> bulk graviton -> HH
#

graviton_hh_vbf_hbb_hmm = graviton_hh_vbf.add_process(
    name="graviton_hh_vbf_hbb_hmm",
    id=32100,
    label=rf"{graviton_hh_vbf.label} $\rightarrow bb\mu\mu$",
    xsecs=multiply_xsecs(graviton_hh_vbf, const.br_hh.bbmm),
)

graviton_hh_vbf_hbb_hmm_m250 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m250",
    id=32101,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m260 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m260",
    id=32102,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m270 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m270",
    id=32103,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m280 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m280",
    id=32104,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m300 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m300",
    id=32105,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m320 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m320",
    id=32106,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m350 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m350",
    id=32107,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m400 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m400",
    id=32108,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m450 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m450",
    id=32109,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m500 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m500",
    id=32110,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m550 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m550",
    id=32111,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m600 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m600",
    id=32112,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m650 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m650",
    id=32113,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m700 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m700",
    id=32114,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m750 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m750",
    id=32115,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m800 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m800",
    id=32116,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m850 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m850",
    id=32117,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m900 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m900",
    id=32118,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m1000 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m1000",
    id=32119,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m1250 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m1250",
    id=32120,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m1500 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m1500",
    id=32121,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m1750 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m1750",
    id=32122,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m2000 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m2000",
    id=32123,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m2500 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m2500",
    id=32124,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)

graviton_hh_vbf_hbb_hmm_m3000 = graviton_hh_vbf_hbb_hmm.add_process(
    name="graviton_hh_vbf_hbb_hmm_m3000",
    id=32125,
    xsecs=graviton_hh_vbf_hbb_hmm.xsecs.copy(),
)
