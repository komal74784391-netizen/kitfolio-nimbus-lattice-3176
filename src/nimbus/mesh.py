def materialise(region, resolution_m, layers=4):
    """Build the tile mesh for one region."""
    return {"region": region, "resolution_m": resolution_m, "layers": layers}
