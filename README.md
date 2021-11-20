# SCons kicad tool

## About

This tool can be used to automate the output of pdf and gerber files from kicad projects with kibot.

## Install

Installing it, requires you to copy (or, even better: checkout) the contents of the
package's ``kicad`` folder to

- ``/path_to_your_project/site_scons/site_tools/kicad``", if you need the `kicad` Tool in one project only, or
- ``/user/share/scons/site_scons/site_tools/kicad``, for a system-wide installation.

For more infos about this, please refer to 

* the SCons User's Guide, sect. "Where to put your custom Builders and Tools"

## Activate the tool

Create a build environment with the kicad builder

```python
env = Environment(tools=['kicad'], 
KICAD_ENVIRONMENT_VARS={'target': {'options': {}, 'layers': {}}})
```
With the `KICAD_ENVIRONMENT_VARS` the kibot utility can be configured.
Allowed targets are: `[pdf_pcb_print] [gerber]`
The other targets can not be configured

### pdf_pcb_print

valid options:
- dnf_filter: [string|list(string)=''] Name of the filter to mark components as not fitted. A short-cut to use for simple cases where a variant is an overkill.
- drill_marks: [string='full'] What to use to indicate the drill places, can be none, small or full (for real scale).
- mirror: [boolean=false] Print mirrored (X axis inverted). ONLY for KiCad 6.
- monochrome: [boolean=false] Print in black and white.
- plot_sheet_reference: [boolean=true] Include the title-block.
- scaling: [number=1.0] Scale factor (0 means autoscaling).
- separated: [boolean=false] Print layers in separated pages.

The layer selection:
- layers: [list(dict)|list(string)|string] [all,selected,copper,technical,user] List of PCB layers to include in the PDF.

### gerber

valid options:
- exclude_edge_layer: [boolean=true] Do not include the PCB edge layer.
- exclude_pads_from_silkscreen: [boolean=false] Do not plot the component pads in the silk screen (KiCad 5.x only).
- plot_sheet_reference: [boolean=false] Currently without effect.
- plot_footprint_refs: [boolean=true] Include the footprint references.
- plot_footprint_values: [boolean=true] Include the footprint values.
- force_plot_invisible_refs_vals: [boolean=false] Include references and values even when they are marked as invisible.
- tent_vias: [boolean=true] Cover the vias.
- use_protel_extensions: [boolean=false] Use legacy Protel file extensions.
- create_gerber_job_file: [boolean=true] Creates a file with information about all the generated gerbers. You can use it in gerbview - to load all gerbers at once.
- disable_aperture_macros: [boolean=false] Disable aperture macros (workaround for buggy CAM software) (KiCad 6).
- gerber_precision: [number=4.6] This the gerber coordinate format, can be 4.5 or 4.6.
- use_gerber_net_attributes: [boolean=true] Include netlist metadata.
- use_gerber_x2_attributes: [boolean=true] Use the extended X2 format (otherwise use X1 formerly RS-274X).
- line_width: [number=0.1] [0.02,2] Line_width for objects without width [mm] (KiCad 5).
- subtract_mask_from_silk: [boolean=false] Substract the solder mask from the silk screen.
- use_aux_axis_as_origin: [boolean=false] Use the auxiliary axis as origin for coordinates.

The layer selection:
- layers: [list(dict)|list(string)|string] [all,selected,copper,technical,user] List of PCB layers to include in the PDF.


## Call the target

example of calling the targets:

```python
REPORTS += env.preflight('report.json', 'board.pro', project_name='project')
env.schema('board_schematic.pdf' % 'board.pro')
env.pcb('board_pcb.pdf' % 'board.pro')
env.gerbers('board_JLCPCB.zip' % 'board.pro')
REPORTS += env.bom('board_bom.json' % 'board.pro' % project_name='kontur')

env.reports('project_reports.json', REPORTS)
```

The `report`target will combine all the outputs from the `preflight` and `bom` targets. The 
files to be combined have to be passed to the target. This can be done with a variable.

When the `project_name` is set it will be used as the top level key in the report. Default
will be `report`.

```json
{
    "project_name": {
            "board": {
                    "bom": [],
                    "erc": [],
                    "drc": [],
                    "unconected": []
            }
    }
} 
```

## Continous Integration

For the integration into a toolset like Jeknins there is the `report2xunit` target. This will convert the reports in the 
json file into a junit xml file that can be processed by the tool. 

```python
env.report2xunit('project_reports.xml', 'project_reports.json')
```
