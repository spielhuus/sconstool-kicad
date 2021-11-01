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
 
import os

import codecs
import zipfile

from sys import path as syspath
syspath.append("/usr/lib/python3.9/site-packages/")

import pcbnew
from pcbnew import *

# def create_gerbers(file_name, output_dir, zip_fname):

#     print("Running KiCAD Plotter CI/CD Script on %s output to %s"%(file_name, output_dir,))

#     try:
#         os.makedirs(output_dir)
#     except OSError:
#         pass


#     board = pcbnew.LoadBoard(file_name)
#     pctl = pcbnew.PLOT_CONTROLLER(board)
#     popt = pctl.GetPlotOptions()
#     popt.SetOutputDirectory(output_dir)
#     popt.SetPlotFrameRef(False)
#     popt.SetLineWidth(pcbnew.FromMM(0.1))

#     popt.SetAutoScale(False)
#     popt.SetScale(1)
#     popt.SetMirror(False)

#     popt.SetUseGerberAttributes(True)
#     popt.SetUseGerberProtelExtensions(True)

#     popt.SetExcludeEdgeLayer(True)
#     popt.SetUseAuxOrigin(False)
#     pctl.SetColorMode(True)

#     popt.SetSubtractMaskFromSilk(False)
#     popt.SetPlotReference(True)
#     popt.SetPlotValue(False)

#     layers = [
#         ("F.Cu", pcbnew.F_Cu, "Top layer"),
#         ("B.Cu", pcbnew.B_Cu, "Bottom layer"),
#         ("F.Paste", pcbnew.F_Paste, "Paste top"),
#         ("B.Paste", pcbnew.B_Paste, "Paste bottom"),
#         ("F.SilkS", pcbnew.F_SilkS, "Silk top"),
#         ("B.SilkS", pcbnew.B_SilkS, "Silk top"),
#         ("F.Mask", pcbnew.F_Mask, "Mask top"),
#         ("B.Mask", pcbnew.B_Mask, "Mask bottom"),
#         ("Edge.Cuts", pcbnew.Edge_Cuts, "Edges"),
#     ]

#     for layer_info in layers:
#         pctl.SetLayer(layer_info[1])
#         pctl.OpenPlotfile(layer_info[0], pcbnew.PLOT_FORMAT_GERBER, layer_info[2])
#         pctl.PlotLayer()
#         pctl.ClosePlot()











layers = ['F.Cu', 'B.Cu', 'F.Adhes', 'B.Adhes']

layer_list = [
    {'name':'F.Cu', 'id':pcbnew.F_Cu, 'fnamekey':'${filename(F.Cu)}'},
    {'name':'B.Cu', 'id':pcbnew.B_Cu, 'fnamekey':'${filename(B.Cu)}'},
    {'name':'F.Adhes', 'id':pcbnew.F_Adhes, 'fnamekey':'${filename(F.Adhes)}'},
    {'name':'B.Adhes', 'id':pcbnew.B_Adhes, 'fnamekey':'${filename(B.Adhes)}'},
    {'name':'F.Paste', 'id':pcbnew.F_Paste, 'fnamekey':'${filename(F.Paste)}'},
    {'name':'B.Paste', 'id':pcbnew.B_Paste, 'fnamekey':'${filename(B.Paste)}'},
    {'name':'F.SilkS', 'id':pcbnew.F_SilkS, 'fnamekey':'${filename(F.SilkS)}'},
    {'name':'B.SilkS', 'id':pcbnew.B_SilkS, 'fnamekey':'${filename(B.SilkS)}'},
    {'name':'F.Mask', 'id':pcbnew.F_Mask, 'fnamekey':'${filename(F.Mask)}'},
    {'name':'B.Mask', 'id':pcbnew.B_Mask, 'fnamekey':'${filename(B.Mask)}'},
    {'name':'Dwgs.User', 'id':pcbnew.Dwgs_User, 'fnamekey':'${filename(Dwgs.User)}'},
    {'name':'Cmts.User', 'id':pcbnew.Cmts_User, 'fnamekey':'${filename(Cmts.User)}'},
    {'name':'Eco1.User', 'id':pcbnew.Eco1_User, 'fnamekey':'${filename(Eco1.User)}'},
    {'name':'Eco2.User', 'id':pcbnew.Eco2_User, 'fnamekey':'${filename(Eco2.User)}'},
    {'name':'Edge.Cuts', 'id':pcbnew.Edge_Cuts, 'fnamekey':'${filename(Edge.Cuts)}'},
    {'name':'F.CrtYd', 'id':pcbnew.F_CrtYd, 'fnamekey':'${filename(F.CrtYd)}'},
    {'name':'B.CrtYd', 'id':pcbnew.B_CrtYd, 'fnamekey':'${filename(B.CrtYd)}'},
    {'name':'F.Fab', 'id':pcbnew.F_Fab, 'fnamekey':'${filename(F.Fab)}'},
    {'name':'B.Fab', 'id':pcbnew.B_Fab, 'fnamekey':'${filename(B.Fab)}'},
    {'name':'In1.Cu', 'id':pcbnew.In1_Cu, 'fnamekey':'${filename(In1.Cu)}'},
    {'name':'In2.Cu', 'id':pcbnew.In2_Cu, 'fnamekey':'${filename(In2.Cu)}'},
    {'name':'In3.Cu', 'id':pcbnew.In3_Cu, 'fnamekey':'${filename(In3.Cu)}'},
    {'name':'In4.Cu', 'id':pcbnew.In4_Cu, 'fnamekey':'${filename(In4.Cu)}'},
    {'name':'In5.Cu', 'id':pcbnew.In5_Cu, 'fnamekey':'${filename(In5.Cu)}'},
    {'name':'In6.Cu', 'id':pcbnew.In6_Cu, 'fnamekey':'${filename(In6.Cu)}'}
]
def refill(board):
    try:
        filler = pcbnew.ZONE_FILLER(board)
        zones = board.Zones()
        filler.Fill(zones)
    except:
        print('Refill Failed')

def forcedel(fname):
    if os.path.exists(fname):
        os.remove(fname)

def forceren(src, dst):
    if(src==dst):
        return
    forcedel(dst)
    if os.path.exists(src):
        os.rename(src, dst)

def getid(s):
    for i in range(len(layer_list)):
        if layer_list[i]['name']==s:
            return layer_list[i]['id']
    return 0

def getindex(s):
    for i in range(len(layer_list)):
        if layer_list[i]['name']==s:
            return i
    return -1

def create_gerbers(board, gerber_dir, zip_fname):

    try:
#        self.settings = self.Get()
        #global zip_fname
        board = pcbnew.LoadBoard(board)
        print(board)
        board_fname = board.GetFileName()
        board_dir = os.path.dirname(board_fname)
        board_basename = (os.path.splitext(
            os.path.basename(board_fname)))[0]
        # gerber_dir = '%s/%s' % (board_dir,
        #                         self.gerberdir.GetValue())
        # zip_fname = '%s/%s' % (
        #     gerber_dir, self.zipfilename.GetValue().replace('*', board_basename))
        if not os.path.exists(gerber_dir):
            os.mkdir(gerber_dir)
        refill(board)
        zipfiles = []
    # PLOT
        print('PlotStart')
        pc = pcbnew.PLOT_CONTROLLER(board)
        po = pc.GetPlotOptions()

        po.SetOutputDirectory(gerber_dir)
        po.SetPlotFrameRef(False)
        #self.settings.get(
        #    'PlotBorderAndTitle', False))
        po.SetPlotValue(True)
        #self.settings.get(
        #    'PlotFootprintValues', True))
        po.SetPlotReference(True)
        #self.settings.get(
        #    'PlotFootprintReferences', True))
        po.SetPlotInvisibleText(False)
#            self.settings.get('ForcePlotInvisible', False))
        po.SetExcludeEdgeLayer(True)
#            self.settings.get('ExcludeEdgeLayer', True))
        if hasattr(po, 'SetPlotPadsOnSilkLayer'):
            po.SetPlotPadsOnSilkLayer(False)
#                not self.settings.get('ExcludePadsFromSilk', False))
        po.SetPlotViaOnMaskLayer(False)
#            self.settings.get('DoNotTentVias', False))
        if hasattr(po, 'SetUseAuxOrigin'):
            po.SetUseAuxOrigin(False)
#                self.settings.get('UseAuxOrigin', False))
        if hasattr(po, 'SetLineWidth'):
            po.SetLineWidth(1)
#                FromMM(float(self.settings.get('LineWidth'))))
        po.SetSubtractMaskFromSilk(True)
#            self.settings.get('SubtractMaskFromSilk', True))
        po.SetUseGerberX2format(False)
#            self.settings.get('UseExtendedX2format', False))
        po.SetIncludeGerberNetlistInfo(False)
#            self.settings.get('IncludeNetlistInfo', False))
        po.SetGerberPrecision(5)
        # if self.settings.get(5)
#            'CoodinateFormat46', True) else 5)

    #                   SetDrillMarksType() : Draw Drill point to Cu layers if 1 (default)
    #                                         But seems set to 0 in Plot Dialog
        po.SetDrillMarksType(0)
        #print('set layers')
        #layer = ['F.Cu'] #self.settings.get('Layers', {})
        #forcedel(zip_fname)
        #for i in range(len(layer_list)):
        #    layer_list[i]['fname'] = ''
        for i in layer_list:
            fnam = i['name']
            #id = getid(i)
#            if(len(fnam) > 0 and board.IsLayerEnabled(id)):
            pc.SetLayer(i['id'])
            pc.OpenPlotfile(i, PLOT_FORMAT_GERBER, i)
            pc.PlotLayer()
            pc.ClosePlot()
            targetname = '%s/%s' % (gerber_dir,
                                    fnam.replace('*', board_basename))
            forcedel(targetname)
            forceren(pc.GetPlotFileName(), targetname)
            layer_list[getindex(i)]['fname'] = targetname
            zipfiles.append(targetname)
        print('Drill')
    # DRILL
        drill_fname = ''
        drill_map_fname = ''
        npth_fname = ''
        npth_map_fname = ''
        drill_report_fname = ''
        drill = {} #self.settings.get('Drill', {})
        fname = drill.get('Drill', '')
        if len(fname) > 0:
            drill_fname = '%s/%s' % (gerber_dir,
                                        fname.replace('*', board_basename))
            forcedel(drill_fname)
        fname = drill.get('DrillMap', '')
        if len(fname) > 0:
            drill_map_fname = '%s/%s' % (gerber_dir,
                                            fname.replace('*', board_basename))
            forcedel(drill_map_fname)
        fname = drill.get('NPTH', '')
        if len(fname) > 0:
            npth_fname = '%s/%s' % (gerber_dir,
                                    fname.replace('*', board_basename))
            forcedel(npth_fname)
        fname = drill.get('NPTHMap', '')
        if len(fname) > 0:
            npth_map_fname = '%s/%s' % (gerber_dir,
                                        fname.replace('*', board_basename))
            forcedel(npth_map_fname)
        fname = drill.get('Report', '')
        if len(fname) > 0:
            drill_report_fname = '%s/%s' % (
                gerber_dir, fname.replace('*', board_basename))
            forcedel(drill_report_fname)

        ew = EXCELLON_WRITER(board)
        excellon_format = EXCELLON_WRITER.DECIMAL_FORMAT
        # zeros = self.settings.get('ZerosFormat')
        # if zeros.get('SuppressLeading'):
        #     excellon_format = EXCELLON_WRITER.SUPPRESS_LEADING
        # if zeros.get('SuppressTrailing'):
        #     excellon_format = EXCELLON_WRITER.SUPPRESS_TRAILING
        # if zeros.get('KeepZeros'):
        #     excellon_format = EXCELLON_WRITER.KEEP_ZEROS
        ew.SetFormat(True, excellon_format, 3, 3)
        #ew.SetFormat(self.settings.get(
        #    'DrillUnitMM', True), excellon_format, 3, 3)
        offset = wxPoint(0, 0)
        # if self.settings.get('UseAuxOrigin', False):
        #     if hasattr(board, 'GetAuxOrigin'):
        #         offset = board.GetAuxOrigin()
        #     else:
        #         bds = board.GetDesignSettings()
        #         offset = bds.m_AuxOrigin
        # ew.SetOptions(self.settings.get('MirrorYAxis', False), self.settings.get(
        #     'MinimalHeader', False), offset, self.settings.get('MergePTHandNPTH', False))
        # ew.SetRouteModeForOvalHoles(
        #     self.settings.get('RouteModeForOvalHoles'))
        map_format = pcbnew.PLOT_FORMAT_GERBER
        map_ext = 'gbr'
        # map = self.settings.get('MapFileFormat')
        # if map.get('HPGL'):
        #     map_format = pcbnew.PLOT_FORMAT_HPGL
        #     map_ext = 'plt'
        # if map.get('PostScript'):
        #     map_format = pcbnew.PLOT_FORMAT_POST
        #     map_ext = 'ps'
        # if map.get('Gerber'):
        #     map_format = pcbnew.PLOT_FORMAT_GERBER
        #     map_ext = 'gbr'
        # if map.get('DXF'):
        #     map_format = pcbnew.PLOT_FORMAT_DXF
        #     map_ext = 'dxf'
        # if map.get('SVG'):
        #     map_format = pcbnew.PLOT_FORMAT_SVG
        #     map_ext = 'svg'
        # if map.get('PDF'):
        map_format = pcbnew.PLOT_FORMAT_PDF
        map_ext = 'pdf'
        #endif
        ew.SetMapFileFormat(map_format)
        enable_map = len(drill_map_fname) > 0 or len(
            npth_map_fname) > 0
        print('MapFile')
        ew.CreateDrillandMapFilesSet(gerber_dir, True, enable_map)
        # if self.settings.get('MergePTHandNPTH', False):
        #     if drill_fname:
        #         forceren('%s/%s.drl' %
        #                     (gerber_dir, board_basename), drill_fname)
        #         zipfiles.append(drill_fname)
        #     if drill_map_fname:
        #         forceren('%s/%s-drl_map.%s' % (gerber_dir,
        #                     board_basename, map_ext), drill_map_fname)
        #         zipfiles.append(drill_map_fname)
        # else:
        if drill_fname:
            forceren('%s/%s-PTH.drl' %
                        (gerber_dir, board_basename), drill_fname)
            zipfiles.append(drill_fname)
        if drill_map_fname:
            forceren('%s/%s-PTH-drl_map.%s' % (gerber_dir,
                        board_basename, map_ext), drill_map_fname)
            zipfiles.append(drill_map_fname)
        if npth_fname:
            forceren('%s/%s-NPTH.drl' %
                        (gerber_dir, board_basename), npth_fname)
            zipfiles.append(npth_fname)
        if npth_map_fname:
            forceren('%s/%s-NPTH-drl_map.gbr' %
                        (gerber_dir, board_basename), npth_map_fname)
            zipfiles.append(npth_map_fname)

        if drill_report_fname:
            ew.GenDrillReportFile(drill_report_fname)
            zipfiles.append(drill_report_fname)

    # OptionalFile
        print('optional')
        files = [] #self.settings.get('OptionalFiles', [])
        for n in range(len(files)):
            if(len(files[n]['name'])):
                optional_fname = '%s/%s' % (gerber_dir,
                                            files[n]['name'])
                optional_content = files[n]['content']
                optional_content = optional_content.replace(
                    '${basename}', board_basename)
                for i in range(len(layer_list)):
                    kpath = '${filepath(' + \
                                        layer_list[i]['name']+')}'
                    kname = '${filename(' + \
                                        layer_list[i]['name']+')}'
                    path = layer_list[i]['fname']
                    name = os.path.basename(path)
                    optional_content = optional_content.replace(
                        kname, name)
                if optional_fname:
                    with codecs.open(optional_fname, 'w', 'utf-8') as f:
                        f.write(optional_content)
                zipfiles.append(optional_fname)

    # ZIP
        #print('Zip')
        with zipfile.ZipFile(zip_fname, 'w', compression=zipfile.ZIP_DEFLATED) as f:
            for i in range(len(zipfiles)):
                fnam = zipfiles[i]
                if os.path.exists(fnam):
                    f.write(fnam, os.path.basename(fnam))

    except Exception as e:
        print(e)
        #s=traceback.format_exc(chain=False)
        #print(s)

if __name__ == '__main__':
    create_gerbers('example/produkt/produkt.kicad_pcb', 'gerbers', 'gerbers.zip')

