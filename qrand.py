{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "9834fc8c-6944-4548-8c21-1a617777c834",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ibmqfactory.load_account:WARNING:2022-01-02 20:29:17,903: Credentials are already in use. The existing account in the session will be replaced.\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Importing standard Qiskit libraries\n",
    "from qiskit import QuantumCircuit, transpile, Aer, IBMQ, assemble\n",
    "from qiskit.tools.jupyter import *\n",
    "from qiskit.visualization import *\n",
    "from ibm_quantum_widgets import *\n",
    "from qiskit.providers.aer import QasmSimulator\n",
    "from qiskit_textbook.problems import dj_problem_oracle\n",
    "\n",
    "# Loading your IBM Quantum account(s)\n",
    "provider = IBMQ.load_account()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1816d417-13e0-406f-bb2c-9fb9a367d1b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def bitcount(counts): \n",
    "    return [k for k, v in counts.items() if v == 1][0]\n",
    "\n",
    "def randint(max):\n",
    "    n = len(bin(max))-2\n",
    "    qc = QuantumCircuit(n, n)\n",
    "    \n",
    "    for i in range(n):\n",
    "        qc.h(i)\n",
    "    \n",
    "    for i in range(n):\n",
    "        qc.measure(i, i)\n",
    "    \n",
    "    aer_sim = Aer.get_backend('aer_simulator')\n",
    "    qobj = assemble(qc, aer_sim)\n",
    "    results = aer_sim.run(qobj, shots=1).result()\n",
    "    answer = bitcount(results.get_counts())\n",
    "    \n",
    "    if int(answer,2) < max:\n",
    "        return int(answer,2)\n",
    "    else:\n",
    "        randint(max)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Qiskit v0.33.1 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {
     "0d046273376c4800b5533f2a3309899f": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {}
     },
     "12a478b06af94494bab68798fe4e0912": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_0d046273376c4800b5533f2a3309899f",
       "style": "IPY_MODEL_6994e8ead7834fffa5d5591b6d47734b",
       "value": "<h5>Message</h5>"
      }
     },
     "18d82945f64a4591ab8dd82b4f8e69a6": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "95px"
      }
     },
     "19fbd6a452ef4616854e69688be1c248": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_b0996ca4d16b4cfcb81ffb6b65406062",
       "style": "IPY_MODEL_85a7ccb1032a4d2f87b8a5689c0612cb",
       "value": "<p style='font-family: IBM Plex Sans, Arial, Helvetica, sans-serif; font-size: 20px; font-weight: medium;'>Circuit Properties</p>"
      }
     },
     "1a3d9e5f04794a47a826d43d5fa9a605": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HBoxModel",
      "state": {
       "children": [
        "IPY_MODEL_32e8c83c3e6744a28d4c2ade29394aa7",
        "IPY_MODEL_c32cb4c4c7fb4f82b5eb8a3ed727bf09",
        "IPY_MODEL_eed24c69c9ec4ab6aedce50cfb2c8bf7",
        "IPY_MODEL_2bc1ca1624ba4dfcbfa31a5140bc2add",
        "IPY_MODEL_12a478b06af94494bab68798fe4e0912"
       ],
       "layout": "IPY_MODEL_e9fb72c06da44edea216c9a0cb4ffb25"
      }
     },
     "2bc1ca1624ba4dfcbfa31a5140bc2add": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_bad02155795440d2a7109b486ec4fec8",
       "style": "IPY_MODEL_90fde94498424237bb54347f6625bb3f",
       "value": "<h5>Queue</h5>"
      }
     },
     "32e8c83c3e6744a28d4c2ade29394aa7": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_d7203a6d1f0e46bcb04a51c6fd722bbb",
       "style": "IPY_MODEL_8084d968a0fd4d69a2ba3edfff73f416",
       "value": "<h5>Job ID</h5>"
      }
     },
     "5d7eef4fa1564eb0be1dcb8a97192d33": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "GridBoxModel",
      "state": {
       "children": [
        "IPY_MODEL_7a0452eaab8b4e1bbe5ecc1989e2ca79"
       ],
       "layout": "IPY_MODEL_f3fa9fd43c8645e1ace3ffd8540da709"
      }
     },
     "60023d1f65034319aaa3b2220e95d00c": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "145px"
      }
     },
     "6994e8ead7834fffa5d5591b6d47734b": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "7a0452eaab8b4e1bbe5ecc1989e2ca79": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "ButtonModel",
      "state": {
       "button_style": "primary",
       "description": "Clear",
       "layout": "IPY_MODEL_d395bad8efa44f8696e023ddf8c9b5b9",
       "style": "IPY_MODEL_9bf6a4b45f2b424183e68cf59cff7071"
      }
     },
     "8084d968a0fd4d69a2ba3edfff73f416": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "85a7ccb1032a4d2f87b8a5689c0612cb": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "90fde94498424237bb54347f6625bb3f": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "9bf6a4b45f2b424183e68cf59cff7071": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "ButtonStyleModel",
      "state": {}
     },
     "a9ecbeb8222045cbadd35cbaa601a5cd": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "b0996ca4d16b4cfcb81ffb6b65406062": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "margin": "0px 0px 10px 0px"
      }
     },
     "bad02155795440d2a7109b486ec4fec8": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "70px"
      }
     },
     "c301d9532a594df3b0e05dfa5400b3de": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "description_width": ""
      }
     },
     "c32cb4c4c7fb4f82b5eb8a3ed727bf09": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_60023d1f65034319aaa3b2220e95d00c",
       "style": "IPY_MODEL_a9ecbeb8222045cbadd35cbaa601a5cd",
       "value": "<h5>Backend</h5>"
      }
     },
     "d395bad8efa44f8696e023ddf8c9b5b9": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "grid_area": "right",
       "padding": "0px 0px 0px 0px",
       "width": "70px"
      }
     },
     "d7203a6d1f0e46bcb04a51c6fd722bbb": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "width": "190px"
      }
     },
     "e9fb72c06da44edea216c9a0cb4ffb25": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "margin": "0px 0px 0px 37px",
       "width": "600px"
      }
     },
     "eed24c69c9ec4ab6aedce50cfb2c8bf7": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "layout": "IPY_MODEL_18d82945f64a4591ab8dd82b4f8e69a6",
       "style": "IPY_MODEL_c301d9532a594df3b0e05dfa5400b3de",
       "value": "<h5>Status</h5>"
      }
     },
     "f3fa9fd43c8645e1ace3ffd8540da709": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "grid_template_areas": "\n                                       \". . . . right \"\n                                        ",
       "grid_template_columns": "20% 20% 20% 20% 20%",
       "width": "100%"
      }
     }
    },
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
