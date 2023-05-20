import aerosandbox as asb

sd7037 = asb.Airfoil("sd7037")

sd7037.generate_polars(cache_filename="./cache/sd7037")
naca0012 = asb.Airfoil("naca0012")
naca0012.generate_polars(cache_filename="./cache/naca0012.json")

airplane = asb.Airplane(
    name="Vanilla",
    xyz_ref=[0.5, 0, 0],
    wings=[
        asb.Wing(
            name="Wing",
            symmetric=True,
            xsecs=[
                asb.WingXSec(
                    xyz_le=[0, 0, 0],
                    chord=1,
                    twist=0,
                    airfoil=naca0012,
                ),
                asb.WingXSec(
                    xyz_le=[0, 0.5, 0],
                    chord=1,
                    twist=0,
                    airfoil=naca0012,
                ),
                asb.WingXSec(
                    xyz_le=[0.3, 3.5, 0],
                    chord=1,
                    twist=0,
                    airfoil=naca0012,
                )
            ]
        )
        # asb.Wing(
        #     name="H-stab",
        #     symmetric=True,
        #     xsecs=[
        #         asb.WingXSec(
        #             xyz_le=[0, 0, 0],
        #             chord=0.7,
        #             airfoil=naca0012,
        #         ),
        #         asb.WingXSec(
        #             xyz_le=[0.14, 1.25, 0],
        #             chord=0.42,
        #             airfoil=naca0012,
        #         ),
        #     ]
        # ).translate([4, 0, 0.6]),
   ]
)

if __name__ == '__main__':
    airplane.draw_three_view()
