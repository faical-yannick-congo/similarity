from simy.features import reshape_feature
import pkg_resources
import json

class TestReshape:

    def test_reshape(self):
        """testing the reshape functionality.
        """

        source = {
           "calculation-relax-static":{
              "key":"00999575-6044-4420-baf5-9bb33e60b02c",
              "calculation":{
                 "iprPy-version":"0.8.3",
                 "atomman-version":"1.2.4",
                 "LAMMPS-version":"22 Aug 2018",
                 "script":"calc_relax_static",
                 "run-parameter":{
                    "size-multipliers":{
                       "a":[
                          0,
                          1
                       ],
                       "b":[
                          0,
                          1
                       ],
                       "c":[
                          0,
                          1
                       ]
                    },
                    "energytolerance":0.0,
                    "forcetolerance":{
                       "value":1e-10,
                       "unit":"eV/angstrom"
                    },
                    "maxiterations":10000,
                    "maxevaluations":100000,
                    "maxatommotion":{
                       "value":0.01,
                       "unit":"angstrom"
                    }
                 }
              },
              "potential-LAMMPS":{
                 "key":"bb69cb78-f906-476f-866a-8411864e5130",
                 "id":"1996--Farkas-D--Nb-Ti-Al--LAMMPS--ipr1",
                 "potential":{
                    "key":"0856888b-57ec-4005-828d-d1b0c331f120",
                    "id":"1996--Farkas-D-Jones-C--Nb-Ti-Al"
                 }
              },
              }
        }

        expected = {
            "calculation-relax-static.calculation.LAMMPS-version": "22 Aug 2018",
            "calculation-relax-static.calculation.atomman-version": "1.2.4",
            "calculation-relax-static.calculation.iprPy-version": "0.8.3",
            "calculation-relax-static.calculation.run-parameter.energytolerance": 0,
            "calculation-relax-static.calculation.run-parameter.forcetolerance.unit": "eV/angstrom",
            "calculation-relax-static.calculation.run-parameter.forcetolerance.value": 1e-10,
            "calculation-relax-static.calculation.run-parameter.maxatommotion.unit": "angstrom",
            "calculation-relax-static.calculation.run-parameter.maxatommotion.value": 0.01,
            "calculation-relax-static.calculation.run-parameter.maxevaluations": 100000,
            "calculation-relax-static.calculation.run-parameter.maxiterations": 10000,
            "calculation-relax-static.calculation.run-parameter.size-multipliers.a.0": 0,
            "calculation-relax-static.calculation.run-parameter.size-multipliers.a.1": 1,
            "calculation-relax-static.calculation.run-parameter.size-multipliers.b.0": 0,
            "calculation-relax-static.calculation.run-parameter.size-multipliers.b.1": 1,
            "calculation-relax-static.calculation.run-parameter.size-multipliers.c.0": 0,
            "calculation-relax-static.calculation.run-parameter.size-multipliers.c.1": 1,
            "calculation-relax-static.calculation.script": "calc_relax_static",
            "calculation-relax-static.key": "00999575-6044-4420-baf5-9bb33e60b02c",
            "calculation-relax-static.potential-LAMMPS.id": "1996--Farkas-D--Nb-Ti-Al--LAMMPS--ipr1",
            "calculation-relax-static.potential-LAMMPS.key": "bb69cb78-f906-476f-866a-8411864e5130",
            "calculation-relax-static.potential-LAMMPS.potential.id": "1996--Farkas-D-Jones-C--Nb-Ti-Al",
            "calculation-relax-static.potential-LAMMPS.potential.key": "0856888b-57ec-4005-828d-d1b0c331f120"
        }
        assert reshape_feature.reshape(expected) == expected
