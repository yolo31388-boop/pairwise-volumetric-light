import pytest
import math
from render import volumetric_light as mod

CASES = [
    ("step", 'm.step_size(10, 0.05) == approx(0.5)'),
    ("dither", 'm.dither(0.5, 0) == approx(0.5)'),
    ("edge", 'm.upsample_edge(0.1, 0.2) is True'),
    ("occ", 'm.occlusion_samples(4) == 4'),
    ("reproj", 'm.reproject((0.5, 0.5), (0.1, 0.2)) == approx((0.4, 0.3))'),
    ("od", 'm.optical_depth(2, 3) == approx(6.0)'),
    ("lights", 'm.multi_light_energy([1, 2]) == 3'),
    ("hdr", 'm.hdr_clamp(1200, 1000) == 1000'),
    ("degrade", 'm.degrade_transmittance(4, 8) == approx(0.5)'),
    ("comp", 'm.layer_composite(0.5, 0.5) == approx(0.75)'),
    ("uv", 'm.valid_uv((0.5, 0.5)) is True'),
    ("phase", 'm.phase_weight(0.5) == approx(0.5)'),
    ("end", 'm.march_end(10, 4) == 4'),
    ("shadow", 'm.sample_shadow(0.8, 0.5) == approx(0.5)'),
    ("id", 'm.light_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
