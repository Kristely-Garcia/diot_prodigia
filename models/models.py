# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class extra-addons/diot_prodigia(models.Model):
#     _name = 'extra-addons/diot_prodigia.extra-addons/diot_prodigia'


class MxReportPartnerLedgerProdigia(models.AbstractModel):
    _inherit = "l10n_mx.account.diot"

    def _l10n_mx_diot_txt_export(self, options):
        txt_data = self.get_lines(options)
        lines = ''
        for line in txt_data:
            if not line.get('id').startswith('partner_'):
                continue
            columns = line.get('columns', [])
            if not sum([c.get('name', 0) for c in columns[5:]]):
                continue
            data = [''] * 25
            data[0] = columns[0]['name']
            data[1] = columns[1]['name']
            data[2] = columns[2]['name'] if columns[0]['name'] == '04' else ''
            data[3] = columns[2]['name'] if columns[0]['name'] != '04' else ''
            data[4] = u''.join(line.get('name', '')).encode(
                'utf-8').strip().decode('utf-8') if columns[0]['name'] != '04' else ''
            data[5] = columns[3]['name'] if columns[0]['name'] != '04' else ''
            data[6] = u''.join(columns[4]['name']).encode(
                'utf-8').strip().decode('utf-8') if columns[0]['name'] != '04' else ''
            data[7] = int(columns[5]['name']) if columns[5]['name'] else ''
            data[9] = int(columns[6]['name']) if columns[6]['name'] else ''
            data[12] = int(columns[7]['name']) if columns[7]['name'] else ''
            data[14] = int(columns[8]['name']) if columns[8]['name'] else ''
            data[20] = int(columns[9]['name']) if columns[9]['name'] else ''
            data[21] = int(columns[10]['name']) if columns[10]['name'] else ''
            data[22] = int(columns[11]['name']) if columns[11]['name'] else ''
            lines += '|'.join(str(d) for d in data) + '\n'
        return lines
