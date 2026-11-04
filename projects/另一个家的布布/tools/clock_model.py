"""Wall clock model matching the approved single-item clock: light-oak ring, white matte face, 12 thin ticks, black hour + minute hands, no second hand.
Faces +Y (into the room), sits on the sofa-back wall. set_time(h, m) turns the hands. 0.30 m face, 0.04 m deep."""
import bpy, math
from mathutils import Vector
CX, CY, CZ = 2.2, -3.575, 1.95          # centre of the clock on the sofa-back wall (metres, project coordinates) - estimated
def mat(name, rgb, rough=0.5):
    m = bpy.data.materials.new(name); m.diffuse_color = (*rgb, 1)       # Workbench shows the viewport colour
    try:
        m.use_nodes = True
        for n in m.node_tree.nodes:
            if n.type == "BSDF_PRINCIPLED": n.inputs["Base Color"].default_value = (*rgb, 1); n.inputs["Roughness"].default_value = rough
    except Exception: pass
    return m
def build():
    for o in list(bpy.data.objects):
        if o.name.startswith("CLOCK_"): bpy.data.objects.remove(o, do_unlink=True)
    root = bpy.data.objects.new("CLOCK_ROOT", None); bpy.context.scene.collection.objects.link(root); root.location = (CX, CY, CZ)
    oak, white, black = mat("clock_oak", (0.75, 0.55, 0.32), 0.55), mat("clock_face", (0.92, 0.92, 0.90), 0.8), mat("clock_black", (0.02, 0.02, 0.02), 0.4)
    def add(name, prim, mt, loc, scale, rot=(0, 0, 0)):
        bpy.ops.mesh.primitive_cylinder_add(vertices=64) if prim == "cyl" else bpy.ops.mesh.primitive_cube_add()
        o = bpy.context.active_object; o.name = "CLOCK_" + name; o.parent = root; o.location = loc; o.scale = scale; o.rotation_euler = rot; o.data.materials.append(mt); return o
    qx = (math.pi / 2, 0, 0)            # cylinder axis -> Y
    add("ring", "cyl", oak, (0, 0.0, 0), (0.160, 0.160, 0.020), qx)        # scale: radius, radius, half-depth (cylinder axis is turned to Y)
    add("face", "cyl", white, (0, 0.0205, 0), (0.145, 0.145, 0.002), qx)
    for i in range(12):
        t = math.radians(30 * i); L = 0.014 if i % 3 else 0.022
        r = 0.145 - L / 2 - 0.004
        add("tick%d" % i, "cube", black, (-math.sin(t) * r, 0.0245, math.cos(t) * r), (0.0016, 0.0006, L / 2), (0, -t, 0))
    for nm, length, wd, y in (("hour", 0.075, 0.0045, 0.0265), ("minute", 0.115, 0.0035, 0.0275)):
        piv = bpy.data.objects.new("CLOCK_%s_pivot" % nm, None); bpy.context.scene.collection.objects.link(piv); piv.parent = root; piv.location = (0, y, 0)
        h = add("%s_hand" % nm, "cube", black, (0, 0, 0), (wd, 0.0006, length / 2)); h.parent = piv; h.location = (0, 0, length / 2 - 0.01)
    add("hub", "cyl", black, (0, 0.029, 0), (0.007, 0.007, 0.002), qx)
def set_time(h, m):
    bpy.data.objects["CLOCK_minute_pivot"].rotation_euler = (0, -math.radians(6 * m), 0)
    bpy.data.objects["CLOCK_hour_pivot"].rotation_euler = (0, -math.radians(30 * (h % 12) + 0.5 * m), 0)
