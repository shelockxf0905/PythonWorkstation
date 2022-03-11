#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: forms.py
@time: 2015/12/30 0030 下午 10:48
"""


from django import forms

class DreamForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id':'dreamcontent',
                'class':'form-control',
                'required':'required',
                'cols':'25',
                'rows':'2'
            }
        )

    )
