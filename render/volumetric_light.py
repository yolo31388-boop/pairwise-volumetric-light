import math

def step_size(depth, base):
    """自适应步长。"""
    raise NotImplementedError("TODO: step_size")

def dither(sample, frame):
    """蓝噪抖动。"""
    raise NotImplementedError("TODO: dither")

def upsample_edge(delta, threshold):
    """上采样保边。"""
    raise NotImplementedError("TODO: upsample_edge")

def occlusion_samples(count):
    """遮挡采样数。"""
    raise NotImplementedError("TODO: occlusion_samples")

def reproject(uv, motion):
    """重投影。"""
    raise NotImplementedError("TODO: reproject")

def optical_depth(density, distance):
    """光学深度。"""
    raise NotImplementedError("TODO: optical_depth")

def multi_light_energy(energies):
    """多光源能量。"""
    raise NotImplementedError("TODO: multi_light_energy")

def hdr_clamp(value, maximum):
    """HDR 限幅。"""
    raise NotImplementedError("TODO: hdr_clamp")

def degrade_transmittance(steps, base_steps):
    """降档透射率。"""
    raise NotImplementedError("TODO: degrade_transmittance")

def layer_composite(a, b):
    """分层合成。"""
    raise NotImplementedError("TODO: layer_composite")

def valid_uv(uv):
    """UV 合法性。"""
    raise NotImplementedError("TODO: valid_uv")

def phase_weight(g):
    """相函数权重。"""
    raise NotImplementedError("TODO: phase_weight")

def march_end(depth, maximum):
    """步进终点。"""
    raise NotImplementedError("TODO: march_end")

def sample_shadow(depth, shadow):
    """阴影采样。"""
    raise NotImplementedError("TODO: sample_shadow")

def light_id(seed, index):
    """体积光 id。"""
    raise NotImplementedError("TODO: light_id")
