#!/usr/bin/env python
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
from kicad import report2xunit

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

def create_pcbdraw_config(env, path, ext) :
    dict = env.get('KICAD_ENVIRONMENT_VARS', {}).get('pdf_pcb_print', {})
    
    conf = {'kibot': {'version': 1}, 
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
        'name': 'pdf_pcb_print',
        'comment': 'Exports the PCB to the most common exchange format. Suitable for printing.',
        'type': 'pdf_pcb_print',
        'options': {
            'output': '%f-pcb.%x',
            'dnf_filter': dict.get('options', {}).get('dnf_filter', ''),
            'drill_marks': dict.get('options', {}).get('dnf_filter', 'full'),
            'mirror': dict.get('options', {}).get('mirror', False),
            'monochrome': dict.get('options', {}).get('monochrome', False),
            'plot_sheet_reference': dict.get('options', {}).get('plot_sheet_reference', True),
            'scaling': dict.get('options', {}).get('scaling', 1.0),
            'separated': dict.get('options', {}).get('separated', False),
            'variant': dict.get('options', {}).get('variant', ''),
            #'hide_excluded': dict.get('options', {}).get('hide_excluded', False),
        },
        'layers': dict.get('layers', [ 
            'F.Cu',
            'B.Cu',
            'B.SilkS',
            'F.SilkS',
            'B.Mask',
            'F.Mask'
        ])
    }]}

    with open(path, 'w') as file:
        file.write(yaml.dump(conf))

    return None

def create_gerbers_jlcbcb_config(env, path) :
    dict = env.get('KICAD_ENVIRONMENT_VARS', {}).get('gerber', {})

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
            'exclude_edge_layer': dict.get('options', {}).get('exclude_edge_layer', True),
            'exclude_pads_from_silkscreen': dict.get('options', {}).get('exclude_pads_from_silkscreen', True),
            'plot_sheet_reference': dict.get('options', {}).get('plot_sheet_reference', False),
            'plot_footprint_refs': dict.get('options', {}).get('plot_footprint_refs', True),
            'plot_footprint_values': dict.get('options', {}).get('plot_footprint_values', False),
            'force_plot_invisible_refs_vals': dict.get('options', {}).get('force_plot_invisible_refs_vals', False),
            'tent_vias': dict.get('options', {}).get('tent_vias', True),
            'use_protel_extensions': dict.get('options', {}).get('use_protel_extensions', False),
            'create_gerber_job_file': dict.get('options', {}).get('create_gerber_job_file', False),
            'disable_aperture_macros': dict.get('options', {}).get('disable_aperture_macros', True),
            'gerber_precision': dict.get('options', {}).get('gerber_precision', 4.6),
            'use_gerber_x2_attributes': dict.get('options', {}).get('use_gerber_x2_attributes', False),
            'use_gerber_net_attributes': dict.get('options', {}).get('use_gerber_net_attributes', False),
            'line_width': dict.get('options', {}).get('line_width', 0.1),
            'subtract_mask_from_silk': dict.get('options', {}).get('subtract_mask_from_silk', True),
            'use_aux_axis_as_origin': dict.get('options', {}).get('use_aux_axis_as_origin', False),
            },
            'layers': dict.get('layers', [ 
            # Note: a more generic approach is to use 'copper' but then the filenames
            # are slightly different.
            'F.Cu',
            'B.Cu',
            'F.SilkS',
            'B.SilkS',
            'F.Mask',
            'B.Mask',
            'Edge.Cuts'
            ])
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

def get_kicad_files(source):
    file = source
    return [file.replace('.pro', '.sch'), file.replace('.pro', '.kicad_pcb')]

def get_kicad_name(source):
    file = Path(source).name
    return file.replace('.pro', '')

def kibot_bom(target, source, env):
    project_name = env.get('project_name', 'report')
    board = get_kicad_name(source[0].path)

    files = get_kicad_files(source[0].abspath)
    conf_file = "%s/kibot_preflight.yaml" % Path(source[0].path).parent
    create_preflight_config(env, conf_file, update_xml=True, run_erc=False, 
                            run_drc=False, check_zone_fills=False, ignore_unconnected=True)
    kibot = 'kibot -q -c kibot_preflight.yaml -b "%s" -e "%s"' % (files[1], files[0])
    env.Execute(kibot, chdir=source[0].get_dir())
    result = {env['project_name']: {board: {}}}
    parse_kibot.bom_parser(("%s/%s.xml" % (source[0].get_dir(), board)), result[project_name][board])
    with open(target[0].abspath, 'w') as file:
        json.dump(result, file)
    os.remove(conf_file)
    os.remove(("%s/%s.xml" % (source[0].get_dir(), board)))
    os.remove(("%s/%s.csv" % (source[0].get_dir(), board)))

    return None

def kibot_preflight(target, source, env):
    project_name = env.get('project_name', 'report')
    board = get_kicad_name(source[0].path)

    files = get_kicad_files(source[0].abspath)
    conf_file = "%s/kibot_preflight.yaml" % Path(source[0].path).parent
    create_preflight_config(env, conf_file)
    kibot = 'kibot -q -c kibot_preflight.yaml -b "%s" -e "%s"' % (files[1], files[0])
    env.Execute(kibot, chdir=source[0].get_dir())
    result = {env['project_name']: {board: {}}}
    parse_kibot.kibot_parser(("%s/%s-drc.txt" % (source[0].get_dir(), board)), result[project_name][board])
    parse_kibot.kibot_parser(("%s/%s-erc.txt" % (source[0].get_dir(), board)), result[project_name][board])
    with open(target[0].abspath, 'w') as file:
        json.dump(result, file)

    os.remove(conf_file)
    os.remove(("%s/%s-drc.txt" % (source[0].get_dir(), board)))
    os.remove(("%s/%s-erc.txt" % (source[0].get_dir(), board)))

    return None

def kibot_schema(target, source, env):

    files = get_kicad_files(source[0].abspath)
    conf_file = "%s/kibot_schema.yaml" % Path(source[0].path).parent
    create_schema_config(env, conf_file)
    kibot = 'kibot -q -c kibot_schema.yaml -b "%s" -e "%s" -s all pdf_sch_print' % (files[1], files[0])
    env.Execute(kibot, chdir=source[0].get_dir())
    os.rename("%s/%s-schematic.pdf" % (source[0].get_dir(), get_kicad_name(source[0].path)), target[0].abspath)
    os.remove(conf_file)
    return None

def kibot_pcb(target, source, env):

    files = get_kicad_files(source[0].abspath)
    conf_file = "%s/kibot_pcbdraw.yaml" % Path(source[0].path).parent
    create_pcbdraw_config(env, conf_file, source[0].suffix)
    kibot = 'kibot -q -c kibot_pcbdraw.yaml -b "%s" -e "%s" -s all pdf_pcb_print' % (files[1], files[0])
    env.Execute(kibot, chdir=source[0].get_dir())
    os.rename(("%s/%s-pcb.pdf" % (source[0].get_dir(), get_kicad_name(source[0].path))), target[0].abspath)
    os.remove(conf_file)
    return None

def kibot_gerbers(target, source, env):

    files = get_kicad_files(source[0].abspath)
    conf_file = "%s/kibot_gerbers.yaml" % Path(source[0].path).parent
    create_gerbers_jlcbcb_config(env, conf_file)
    kibot = 'kibot -q -c kibot_gerbers.yaml -b "%s" -e "%s" -s all JLCPCB' % (files[1], files[0])
    env.Execute(kibot, chdir=source[0].get_dir())
    os.rename(("%s/JLCPCB/%s-JLCPCB.zip" % (source[0].get_dir(), get_kicad_name(source[0].path))), target[0].abspath)
    shutil.rmtree('%s/JLCPCB' % source[0].get_dir())
    os.remove(conf_file)
    return None

def kibot_combine_reports(target, source, env):
    source_files = []
    for s in source :
        source_files.append(s.abspath)

    with open(target[0].abspath, 'w') as file:
        json.dump(parse_kibot.combine_reports(source_files), file)

def xunit(target, source, env):
        report2xunit.convert(source[0].abspath, target[0].abspath)

def generate(env):

    env.SetDefault(KICAD_CONTEXT={})
    env.SetDefault(KICAD_ENVIRONMENT_VARS={})
    env.SetDefault(KICAD_TEMPLATE_SEARCHPATH=[])

    env['BUILDERS']['preflight'] = SCons.Builder.Builder(action=kibot_preflight)
    env['BUILDERS']['schema'] = SCons.Builder.Builder(action=kibot_schema)
    env['BUILDERS']['pcb'] = SCons.Builder.Builder(action=kibot_pcb)
    env['BUILDERS']['gerbers'] = SCons.Builder.Builder(action=kibot_gerbers)
    env['BUILDERS']['bom'] = SCons.Builder.Builder(action=kibot_bom)
    env['BUILDERS']['reports'] = SCons.Builder.Builder(action=kibot_combine_reports)
    env['BUILDERS']['report2xunit'] = SCons.Builder.Builder(action=xunit)

def exists(env):
    try:
        import eeschema
    except ImportError as e:
        raise StopError(ImportError, e.message) 
