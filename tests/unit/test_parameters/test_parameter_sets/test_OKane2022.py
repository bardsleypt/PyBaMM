#
# Tests for O'Kane (2020) parameter set
#
import pybamm
import unittest
import os


class TestOKane2022(unittest.TestCase):
    def test_load_params(self):
        Li_plating = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium_ion/lithium_platings/okane2022_Li_plating/"
                "parameters.csv"
            )
        )
        self.assertEqual(
            Li_plating["Lithium metal partial molar volume [m3.mol-1]"], "1.30E-05"
        )

    def test_functions(self):
        root = pybamm.root_dir()
        param = pybamm.ParameterValues("OKane2022")
        T = pybamm.Scalar(298.15)

        p = "pybamm/input/parameters/lithium_ion/lithium_platings/okane2022_Li_plating/"
        k_path = os.path.join(root, p)

        fun_test = {
            "plating_exchange_current_density_OKane2020.py": ([1e3, 1e4, T], 9.6485e-2),
            "stripping_exchange_current_density_OKane2020.py": (
                [1e3, 1e4, T],
                9.6485e-1,
            ),
            "SEI_limited_dead_lithium_OKane2022.py": ([1e-8], 5e-7)
        }

        for name, value in fun_test.items():
            fun = pybamm.load_function(os.path.join(k_path, name))
            self.assertAlmostEqual(param.evaluate(fun(*value[0])), value[1], places=4)


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
