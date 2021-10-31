# sconstool-kicad

scons tool for kicad build automation

# Installation

Dependencies:
- 
-
-
-


Download or clone this repository and move the kicad directory to the scons site tools folder.

'''
mkdir -p /usr/share/scons/site_scons/site_tools/
mv sconstool-kicad/kicad /usr/share/scons/site_scons/site_tools/
'''

# basic usage

Build an environment with the kicad tool. Options are set in KICAD_ENVIRONMENT_VARS.

'''
env = Environment(ENV = os.environ,
        tools=['default', 'kicad'], 
        KICAD_ENVIRONMENT_VARS={...})
'''

It is important that you pass the os.environ, otherwise kicad will not work correctly.

Call the targets from your SConstruct or SConsScript file.

'''
env.preflight('project_report.json', kicad_project.pro)
env.schema('project_schematic.pdf', kicad_project.pro)
env.pcb('project_pcb.svg', kicad_project.pro)
env.gerbers('project_JLCPCB.zip', kicad_project.pro)
env.bom('project_bom.json', kicad_project.pro)
'''

# configuration

## general options

- output_path set the output path of the kibot tool. This can also be relative to the kicad files.

# TODO 

- implement options
- get pcbdraw inage type from file extension

# links

