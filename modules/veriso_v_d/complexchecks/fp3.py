 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import os
import sys
import traceback

from veriso.base.utils.loadlayer import LoadLayer

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        
        self.root = QgsProject.instance().layerTreeRoot()        
        self.layer_loader = LoadLayer(self.iface)

    def run(self):        
        self.settings = QSettings("CatAIS","VeriSO")
        project_id = self.settings.value("project/id")
        epsg = self.settings.value("project/epsg")
        self.project_dir = self.settings.value("project/projectdir")        
        self.project_id = self.settings.value("project/id")

        locale = QSettings().value('locale/userLocale')[0:2] # this is for multilingual legends
        
        # If locale is different to frence or italian, german will be used.
        # Otherwise we get into troubles with the legends, e.g. locale = "en" but 
        # there is no english legend (qml file).
        if locale == "fr":
            pass
        elif locale == "it":
            pass
        else:
            locale = "de"

        if not project_id:
            self.iface.messageBar().pushMessage("Error",  _translate("VeriSO_V+D_FP3", "project_id not set", None), level=QgsMessageBar.CRITICAL, duration=5)                                
            return

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            group = _translate("VeriSO_V+D_FP3", "FixpunkteKategorie3", None)
            group += " (" + str(project_id) + ")"
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = _translate("VeriSO_V+D_FP3", "Toleranzstufen", None) # Translate with Qt Linguist. German translation not necessary since this text will be used when language is missing.
            layer["featuretype"] = "tseinteilung_toleranzstufe"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "tseinteilung/toleranzstufe_"+locale+".qml"
            
            # Visibility and if legend and/or groupd should be collapsed can
            # be set with parameters in the self.layer_loader.load()
            # method:
            # load(layer, visibility=True, collapsed_legend=False, collapsed_group=False)
            vlayer = self.layer_loader.load(layer)
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = _translate("VeriSO_V+D_FP3", "LFP3 Nachführung", None)
            layer["featuretype"] = "fixpunktekategorie3_lfp3nachfuehrung"
            layer["geom"] = "perimeter" # If no geometry attribute is set, the layer will be loaded as geoemtryless.
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            
            vlayer_lfp3_nf = self.layer_loader.load(layer, False, True)            
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = _translate("VeriSO_V+D_FP3", "LFP3", None)
            layer["featuretype"] = "fixpunktekategorie3_lfp3"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            layer["style"] = "fixpunkte/lfp3_"+locale+".qml"

            vlayer_lfp3 = self.layer_loader.load(layer)
            
            # Join two layers (lfp3 and lfp3nachfuehrung)
            lfp3_field = "entstehung"
            lfp3_nf_field = "ogc_fid"
            join_obj = QgsVectorJoinInfo()
            join_obj.joinLayerId = vlayer_lfp3_nf.id()
            join_obj.joinFieldName = lfp3_nf_field
            join_obj.targetFieldName = lfp3_field
            join_obj.memoryCache = True
            join_obj.prefix = "lfp3_nf_"
            vlayer_lfp3.addJoin(join_obj)
    
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = _translate("VeriSO_V+D_FP3", "LFP3 ausserhalb Gemeinde", None)
            layer["featuretype"] = "t_lfp3_ausserhalb_gemeinde"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            layer["style"] = "fixpunkte/lfp3ausserhalb.qml"
            
            vlayer = self.layer_loader.load(layer)
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = _translate("VeriSO_V+D_FP3", "LFP3 pro TS", None)
            layer["featuretype"] = "t_lfp3_pro_ts"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            
            vlayer_lfp3_pro_ts = self.layer_loader.load(layer)            
        
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = _translate("VeriSO_V+D_FP3", "Gemeindegrenze", None)
            layer["featuretype"] = "gemeindegrenzen_gemeindegrenze"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "gemeindegrenze/gemgre_strichliert.qml"

            gemgrelayer = self.layer_loader.load(layer)
            
            # Change map extent.
            # Bug (?) in QGIS: http://hub.qgis.org/issues/10980
            # Closed for the lack of feedback. Upsi...
            # Still a problem? (sz / 2015-04-12)
            # sz / 2015-04-20: 
            # Aaaah: still a problem. Some really strange combination of checked/unchecked-order-of-layers-thing?
            # If wms is addes after gemgre then is scales (rect.scale(5))?!
            # So it seems that the last added layer HAS TO BE unchecked?
            # No not exactly. Only if a wms is added before?
            # rect.scale(5) has no effect?
            
            # I reopened the ticket / 2015-04-20 / sz
            
            if gemgrelayer:
                rect = gemgrelayer.extent()
                rect.scale(5)
                self.iface.mapCanvas().setExtent(rect)        
                self.iface.mapCanvas().refresh() 
            # Sometimes it does make much more sense
            # to zoom to maximal extent:
            # self.iface.mapCanvas().zoomToFullExtent()
            
            self.export_to_excel(vlayer_lfp3_pro_ts)
        
        
        except Exception:
            QApplication.restoreOverrideCursor()            
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.iface.messageBar().pushMessage("Error", str(traceback.format_exc(exc_traceback)), level=QgsMessageBar.CRITICAL, duration=5)                    
        QApplication.restoreOverrideCursor()


    def export_to_excel(self, vlayer):
        try:
            import xlsxwriter
        except Exception, e:
            self.iface.messageBar().pushMessage("Error", str(e), level=QgsMessageBar.CRITICAL, duration=10)                    
            return        

        # Create excel file.
        filename = QDir.convertSeparators(QDir.cleanPath(os.path.join(self.project_dir, "lfp3_pro_ts.xlsx")))     
        workbook = xlsxwriter.Workbook(filename)
        fmt_bold = workbook.add_format({'bold': True, 'font_name':'Cadastra'})
        fmt_bold_border = workbook.add_format({'bold': True, 'border': 1, 'font_name':'Cadastra'})
        fmt_border = workbook.add_format({'border': 1, 'font_name':'Cadastra'})
        fmt_border_decimal = workbook.add_format({'border': 1, 'font_name':'Cadastra', 'num_format':'0.00'})
        fmt_header = workbook.add_format({'bg_color': '#CACACA', 'border': 1, 'font_name':'Cadastra'})
        fmt_italic = workbook.add_format({'italic': True, 'border': 1, 'font_name':'Cadastra'})
        fmt_sum = workbook.add_format({'bold': True, 'font_color': 'blue', 'border': 1, 'font_name':'Cadastra'})
        fmt_sum_decimal = workbook.add_format({'bold': True, 'font_color': 'blue', 'border': 1, 'font_name':'Cadastra', 'num_format':'0.00'})

        # Create the worksheet for the points defects.
        worksheet = workbook.add_worksheet( _translate("VeriSO_V+D_FP3", u'LFP3 pro TS', None))
        worksheet.set_paper(9)
        worksheet.set_portrait()

        # Write project name into worksheet.
        worksheet.write(0, 0,  _translate("VeriSO_V+D_FP3", "Operat: ", None), fmt_bold)
        worksheet.write(0, 1,  self.project_id, fmt_bold)
        
        # Write headers.
        worksheet.write(4, 0,  _translate("VeriSO_V+D_FP3", "Toleranzstufe", None), fmt_header)
        worksheet.write(4, 1,  _translate("VeriSO_V+D_FP3", "Fläche TS [ha]", None), fmt_header)
        worksheet.write(4, 2,  _translate("VeriSO_V+D_FP3", "Ist-Anzahl LFP3", None), fmt_header)
        worksheet.write(4, 3,  _translate("VeriSO_V+D_FP3", "Soll-Anzahl LFP3", None), fmt_header)
        worksheet.write(4, 4,  _translate("VeriSO_V+D_FP3", "Ist-Soll LFP3", None), fmt_header)

        # Loop through features and add them to worksheet.
        iter = vlayer.getFeatures()
        j = 0

        ts_idx = vlayer.fieldNameIndex("toleranzstufe")
        area_idx = vlayer.fieldNameIndex("flaeche")
        current_idx = vlayer.fieldNameIndex("ist_anzahl")
        target_idx = vlayer.fieldNameIndex("soll_anzahl")
        
        start_row = 5
        sum_area = 0
        sum_current = 0
        sum_target = 0
        sum_diff = 0
        for feature in iter:
            ts = feature.attributes()[ts_idx]
            area = feature.attributes()[area_idx]
            current = feature.attributes()[current_idx]
            target = feature.attributes()[target_idx]
            
            worksheet.write(start_row+j, 0, ts, fmt_bold_border)
            worksheet.write(start_row+j, 1, area, fmt_border_decimal)
            worksheet.write(start_row+j, 2, current, fmt_border)
            worksheet.write(start_row+j, 3, target, fmt_border)
            worksheet.write(start_row+j, 4, (current - target), fmt_border)
            
            sum_area += area
            sum_current += current
            sum_target += target
            sum_diff += (current - target)
            
            j += 1 

        # do not forget sum/total
        worksheet.write(start_row+j, 0,  _translate("VeriSO_V+D_FP3", "Total", None), fmt_bold_border)
        worksheet.write(start_row+j, 1, sum_area, fmt_sum_decimal)
        worksheet.write(start_row+j, 2, sum_current, fmt_sum)
        worksheet.write(start_row+j, 3, sum_target, fmt_sum)
        worksheet.write(start_row+j, 4, sum_diff, fmt_sum)

        # Close excel file.
        workbook.close()
