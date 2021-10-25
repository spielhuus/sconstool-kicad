#
# Copyright (c) 2013 Henry Gomersall <heng@kedevelopments.co.uk>
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

from pathlib import Path

from parse_kibot import kibot_parser

def create_kibot_config(env, path) :

    config = '''kibot:
  version: 1

preflight:
  run_erc: %s
  update_xml: %s
  run_drc: %s
  check_zone_fills: %s
  ignore_unconnected: %s

''' % ('true', 'true','true','true','true')
    
    with open(path, 'w') as file:
        file.write(config)

# class FileSystemLoaderRecorder(FileSystemLoader):
#     ''' A wrapper around FileSystemLoader that records files as they are
#     loaded. These are contained within loaded_filenames set attribute.
#     '''
#     def __init__(self, searchpath, encoding='utf-8'):

#         self.loaded_filenames = set()
#         super(FileSystemLoaderRecorder, self).__init__(searchpath, encoding)

#     def get_source(self, environment, template):
#         '''Overwritten FileSystemLoader.get_source method that extracts the
#         filename that is used to load each filename and adds it to 
#         self.loaded_filenames.
#         '''
#         for searchpath in self.searchpath:
#             filename = os.path.join(searchpath, template)
#             f = open_if_exists(filename)
#             if f is None:
#                 continue
#             try:
#                 contents = f.read().decode(self.encoding)
#             finally:
#                 f.close()

#             self.loaded_filenames.add(filename)

#             return super(FileSystemLoaderRecorder, self).get_source(
#                     environment, template)

#         # If the template isn't found, then we have to drop out.
#         raise TemplateNotFound(template)

def nbconvert_scanner(node, env, path):

    print("nbconvert scanner")

    # Instantiate the file as necessary
    node.get_text_contents()

    node_dir = os.path.dirname(str(node))

    template_dir, filename = os.path.split(str(node))

    template_search_path = ([template_dir] +
            env.subst(env['NBCONVERT_TEMPLATE_SEARCHPATH']))
    print("template search path %s " % template_search_path)
    # template_loader = FileSystemLoaderRecorder(template_search_path)
    
    # jinja_env = jinja2.Environment(loader=template_loader, 
    #         extensions=['jinja2.ext.do'], **env['JINJA_ENVIRONMENT_VARS'])
    # try:
    #     template = jinja_env.get_template(filename)
    # except TemplateNotFound as e:
    #     raise StopError('Missing template: ' + 
    #             os.path.join(template_dir, str(e)))

    # We need to render the template to do all the necessary loading.
    #
    # It's necessary to respond to missing templates by grabbing 
    # the content as the exception is raised. This makes sure of the
    # existence of the file upon which the current scanned node depends.
    #
    # I suspect that this is pretty inefficient, but it does 
    # work reliably.
    context = env['NBCONVERT_CONTEXT']

    # last_missing_file = ''
    # while True:

    #     try:
    #         template.render(**context)
    #     except TemplateNotFound as e:
    #         if last_missing_file == str(e):
    #             # We've already been round once for this file, 
    #             # so need to raise
    #             raise StopError('Missing template: ' + 
    #                     os.path.join(template_dir, str(e)))

    #         last_missing_file = str(e)
    #         # Find where the template came from (using the same ordering
    #         # as Jinja uses).
    #         for searchpath in template_search_path:
    #             filename = os.path.join(searchpath, last_missing_file)
    #             if os.path.exists(filename):
    #                 continue
    #             else:
    #                 env.File(filename).get_text_contents()
    #         continue

    #     break

    # Get all the files that were loaded. The set includes the current node,
    # so we remove that.
    # found_nodes_names = list(template_loader.loaded_filenames)
    # try:
    #     found_nodes_names.remove(str(node))
    # except ValueError as e:
    #     raise StopError('Missing template node: ' + str(node))
    
    # return [env.File(f) for f in found_nodes_names]
    return []

def get_kicad_files(source):
    file = source
    return [file.replace('.pro', '.sch'), file.replace('.pro', '.kicad_pcb')]


def kicad_builder(target, source, env):

    files = get_kicad_files(source[0].path)
    kibot = 'kibot -c _kibot.yaml -b "%s" -e "%s" -d "%s"' % (files[1], files[0], target[0].get_path())
    env.Execute(kibot)

    # output_str = ''

    # for template_file in source:

    #     template_dir, filename = os.path.split(str(template_file))

    #     template_search_path = ([template_dir] +
    #             env.subst(env['JINJA_TEMPLATE_SEARCHPATH']))
    #     template_loader = FileSystemLoaderRecorder(template_search_path)

    #     jinja_env = jinja2.Environment(loader=template_loader, 
    #         extensions=['jinja2.ext.do'], **env['JINJA_ENVIRONMENT_VARS'])

    #     template = jinja_env.get_template(filename)

    #     context = env['JINJA_CONTEXT']
    #     template.render(**context)

    #     output_str += template.render(**context)

    # with open(str(target[0]), 'w') as target_file:
    #     target_file.write(output_str)

    return None

def generate(env):

    env.SetDefault(KICAD_CONTEXT={})
    env.SetDefault(KICAD_ENVIRONMENT_VARS={})
    env.SetDefault(KICAD_TEMPLATE_SEARCHPATH=[])

    env['BUILDERS']['kicad'] = SCons.Builder.Builder(
            action=kicad_builder)

    create_kibot_config(env, '_kibot.yaml')
#    scanner = env.Scanner(function=nbconvert_scanner,
#            skeys=['.ipynb'])

#    env.Append(SCANNERS=scanner)

def exists(env):
    print("test library")
    # try:
    #     import nbconvert
    # except ImportError as e:
    #     raise StopError(ImportError, e.message) 
