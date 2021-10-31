#
# Copyright (c) 2021 spielhuus <spielhuus@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import SCons.Builder
import SCons.Tool
from SCons.Errors import StopError

import os
import shutil
import json
import yaml

import subprocess
from pathlib import Path

from kicad import parse_kibot

def create_preflight_config(env, path, update_xml=False, run_erc=True, run_drc=True, 
                            check_zone_fills=True, ignore_unconnected=False) :
    with open(path, 'w') as file:
        file.write(yaml.dump({'kibot': {'version': 1}, 
    'preflight': 
        {
         'run_erc': run_erc, 
         'update_xml':update_xml, 
         'run_drc': run_drc, 
         'check_zone_fills': check_zone_fills, 
         'ignore_unconnected': ignore_unconnected
        }
    }))
    return None

def create_schema_config(env, path) :
    with open(path, 'w') as file:
        file.write(yaml.dump({'kibot': {'version': 1}, 
    'preflight': 
        {
         'run_erc': False, 
         'update_xml':False, 
         'run_drc': False, 
         'check_zone_fills': False, 
         'ignore_unconnected': True
        },
    'outputs': [
        {
        'name': 'pdf_sch_print',
        'comment': 'Exports the PCB to the most common exchange format. Suitable for printing.',
        'type': 'pdf_sch_print'
        }
    ]}))
    return None

def create_pcbdraw_config(env, path) :
    with open(path, 'w') as file:
        file.write(yaml.dump({'kibot': {'version': 1}, 
    'preflight': 
        {
         'run_erc': False, 
         'update_xml':False, 
         'run_drc': False, 
         'check_zone_fills': False, 
         'ignore_unconnected': True
        },
    'outputs': [
        {
        'name': 'pcbdraw_main',
        'comment': 'Exports the PCB as a 2D model (SVG, PNG or JPG).',
        'type': 'pcbdraw',
        #dir: 'Example/pcbdraw_dir'
        'options': {
        # [boolean=false] render the bottom side of the board (default is top side)
        'bottom': False,
        # [string|list(string)=''] Name of the filter to mark components as not fitted.
        # A short-cut to use for simple cases where a variant is an overkill
        #dnf_filter: ''
        # [number=300] [10,1200] dots per inch (resolution) of the generated image
        'dpi': 1200,
        # [string='svg'] [svg,png,jpg] output format. Only used if no `output` is specified
        'format': 'svg',
        # [list(string)=[]] list of components to highlight
        'highlight': [],
        # [list(string)=[]] list of libraries
        'libs': ['default', 'elektrophon', 'others'],
        # [boolean=false] mirror the board
        'mirror': False,
        # [boolean=false] do not make holes transparent
        'no_drillholes': False,
        # [string='%f-%i%v.%x'] name for the generated file. Affected by global options
        'output': '%f-%i%v.%x',
        # [boolean=false] show placeholder for missing components
        'placeholder': False,
        # [dict|None] replacements for PCB references using components (lib:component)
        #remap:
        # [list(string)|string=none] [none,all] list of components to draw, can be also a string for none or all.
        # The default is none
        'show_components': 'all',
        # [string|dict] PCB style (colors). An internal name, the name of a JSON file or the style options
        'style': {
            # [string='#4ca06c'] color for the board without copper (covered by solder mask)
            'board': '#f0f0f0',
            # [string='#9c6b28'] color for the PCB core (not covered by solder mask)
            'clad': '#9c6b28',
            # [string='#417e5a'] color for the copper zones (covered by solder mask)
            'copper': '#417e5a',
            # [boolean=false] highlight over the component (not under)
            'highlight_on_top': False,
            # [number=1.5] [0,1000] how much the highlight extends around the component [mm]
            'highlight_padding': 1.5,
            # [string='stroke:none;fill:#ff0000;opacity:0.5;'] SVG code for the highlight style
            'highlight_style': 'stroke:none;fill:#ff0000;opacity:0.5;',
            # [string='#000000'] color for the outline
            'outline': '#000000',
            # [string='#b5ae30'] color for the exposed pads (metal finish)
            'pads': '#b5ae30',
            # [string='#f0f0f0'] color for the silk screen
            'silk': '#000000',
            # [string='#bf2600'] color for the V-CUTS
            'vcut': '#bf2600'
        },
        # [string=''] Board variant to apply
        'variant': '',
        # [boolean=false] render V-CUTS on the Cmts.User layer
        'vcuts': False,
        # [string='visible'] [visible,all,none] using visible only the warnings about components in the visible side are generated
        'warnings': 'visible'
        }}
    ]}))
    return None

def create_gerbers_jlcbcb_config(env, path) :
    with open(path, 'w') as file:
        file.write(yaml.dump({'kibot': {'version': 1}, 
    'preflight': 
        {
         'run_erc': False, 
         'update_xml':False, 
         'run_drc': False, 
         'check_zone_fills': False, 
         'ignore_unconnected': True
        },
    'outputs': [
        {
        'name': 'JLCPCB_gerbers',
        'comment': 'Gerbers compatible with JLCPCB',
        'type': 'gerber',
        'dir': 'JLCPCB',
        'options': {#&gerber_options
            'exclude_edge_layer': True,
            'exclude_pads_from_silkscreen': True,
            'plot_sheet_reference': False,
            'plot_footprint_refs': True,
            'plot_footprint_values': False,
            'force_plot_invisible_refs_vals': False,
            'tent_vias': True,
            'use_protel_extensions': False,
            'create_gerber_job_file': False,
            'disable_aperture_macros': True,
            'gerber_precision': 4.6,
            'use_gerber_x2_attributes': False,
            'use_gerber_net_attributes': False,
            'line_width': 0.1,
            'subtract_mask_from_silk': True,
            },
            'layers': [
            # Note: a more generic approach is to use 'copper' but then the filenames
            # are slightly different.
            'F.Cu',
            'B.Cu',
            'F.SilkS',
            'B.SilkS',
            'F.Mask',
            'B.Mask',
            'Edge.Cuts'
            ]
        },
        {
        'name': 'JLCPCB_drill',
        'comment':' Drill files compatible with JLCPCB',
        'type': 'excellon',
        'dir': 'JLCPCB',
        'options': {
            'pth_and_npth_single_file': False,
            'pth_id': '-PTH',
            'npth_id': '-NPTH',
            'metric_units': False,
            'output': "%f%i.%x"
            }
        },
        {
        'name': 'JLCPCB',
        'comment': 'ZIP file for JLCPCB',
        'type': 'compress',
        'dir': 'JLCPCB',
        'options': {
            'files': [
                {'from_output': 'JLCPCB_gerbers',
                'dest': '/'},
                {'from_output': 'JLCPCB_drill',
                'dest': '/'}
                ]
            }
        }
    ]}
    ))
    return None

# def create_kibot_config(env, path) :

#     config = '''kibot:
#   version: 1

# preflight:
#   run_erc: %s
#   update_xml: %s
#   run_drc: %s
#   check_zone_fills: %s
#   ignore_unconnected: %s

# ''' % ('true', 'true','true','true','true')
    
#     with open(path, 'w') as file:
#         file.write(config)

def get_kicad_files(source):
    file = source
    return [file.replace('.pro', '.sch'), file.replace('.pro', '.kicad_pcb')]

def get_kicad_name(source):
    file = Path(source).name
    return file.replace('.pro', '')

def kibot_bom(target, source, env):

    files = get_kicad_files(source[0].path)
    create_preflight_config(env, "kibot_preflight.yaml", update_xml=True, run_erc=False, 
                            run_drc=False, check_zone_fills=False, ignore_unconnected=True)
    kibot = 'kibot -q -c %s -b "%s" -e "%s"' % ("kibot_preflight.yaml", files[1], files[0])
    env.Execute(kibot)
    with open(target[0].path, 'w') as file:
        json.dump(parse_kibot.bom_parser(("%s.xml" % get_kicad_name(source[0].path))), file)
    os.remove("kibot_preflight.yaml")
    os.remove(("%s.xml" % get_kicad_name(source[0].path)))
    os.remove(("%s.csv" % get_kicad_name(source[0].path)))

    return None

def kibot_preflight(target, source, env):

    files = get_kicad_files(source[0].path)
    create_preflight_config(env, "kibot_preflight.yaml")
    kibot = 'kibot -q -c %s -b "%s" -e "%s"' % ("kibot_preflight.yaml", files[1], files[0])
    env.Execute(kibot)
    with open(target[0].path, 'w') as file:
        result = []
        result.append(parse_kibot.kibot_parser(("%s-drc.txt" % get_kicad_name(source[0].path))))
        result.append(parse_kibot.kibot_parser(("%s-erc.txt" % get_kicad_name(source[0].path))))
        json.dump(result, file)

    os.remove("kibot_preflight.yaml")
    os.remove(("%s-drc.txt" % get_kicad_name(source[0].path)))
    os.remove(("%s-erc.txt" % get_kicad_name(source[0].path)))

    return None

def kibot_schema(target, source, env):

    files = get_kicad_files(source[0].path)
    create_schema_config(env, "kibot_schema.yaml")
    kibot = 'kibot -q -c %s -s all pdf_sch_print -b "%s" -e "%s"' % ("kibot_schema.yaml", files[1], files[0])
    env.Execute(kibot)
    os.rename(("%s-schematic.pdf" % get_kicad_name(source[0].path)), target[0].path)
    os.remove("kibot_schema.yaml")
    return None

def kibot_pcb(target, source, env):

    files = get_kicad_files(source[0].path)
    create_pcbdraw_config(env, "kibot_pcbdraw.yaml")
    kibot = 'kibot -q -c %s -s all pcbdraw_main -b "%s" -e "%s"' % ('kibot_pcbdraw.yaml', files[1], files[0])
    env.Execute(kibot)
    os.rename(("%s-top.svg" % get_kicad_name(source[0].path)), target[0].path)
    os.remove("kibot_pcbdraw.yaml")
    return None

def kibot_gerbers(target, source, env):

    files = get_kicad_files(source[0].path)
    create_gerbers_jlcbcb_config(env, "kibot_gerbers.yaml")
    kibot = 'kibot -q -c %s -s all JLCPCB -b "%s" -e "%s"' % ("kibot_gerbers.yaml", files[1], files[0])
    env.Execute(kibot)
    os.rename(("JLCPCB/%s-JLCPCB.zip" % get_kicad_name(source[0].path)), target[0].path)
    shutil.rmtree('JLCPCB')
    os.remove("kibot_gerbers.yaml")
    return None

def generate(env):

    print("generate kicad")
    env.SetDefault(KICAD_CONTEXT={})
    env.SetDefault(KICAD_ENVIRONMENT_VARS={})
    env.SetDefault(KICAD_TEMPLATE_SEARCHPATH=[])

    env['BUILDERS']['preflight'] = SCons.Builder.Builder(action=kibot_preflight)
    env['BUILDERS']['schema'] = SCons.Builder.Builder(action=kibot_schema)
    env['BUILDERS']['pcb'] = SCons.Builder.Builder(action=kibot_pcb)
    env['BUILDERS']['gerbers'] = SCons.Builder.Builder(action=kibot_gerbers)
    env['BUILDERS']['bom'] = SCons.Builder.Builder(action=kibot_bom)

def exists(env):
    print("test library")
    result = subprocess.run(['kibot', '--version'], stdout=subprocess.PIPE)
    print(result.stdout)

    # try:
    #     import nbconvert
    # except ImportError as e:
    #     raise StopError(ImportError, e.message) 
