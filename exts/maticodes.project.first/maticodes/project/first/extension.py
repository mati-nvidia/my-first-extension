import omni.ext
import omni.ui as ui
import omni.usd
from pxr import UsdGeom

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[maticodes.project.first] MyExtension startup")

        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                ui.Label("Some Label")

                def on_click():
                    print("created cube!")
                    stage = omni.usd.get_context().get_stage()
                    selection = omni.usd.get_context().get_selection()
                    for prim_path in selection.get_selected_prim_paths():
                        parent = stage.GetPrimAtPath(prim_path)
                        cube = UsdGeom.Cube.Define(stage, parent.GetPath().AppendPath("Cube"))

                ui.Button("Create Cubes", clicked_fn=lambda: on_click())

    def on_shutdown(self):
        print("[maticodes.project.first] MyExtension shutdown")
