# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-05 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0036_auto_20171005_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree_programme_2',
            field=models.CharField(choices=[('', '-'), ('AACOM', 'Bachelor of Advanced Computing (Honours)'), ('AACRD', 'Bachelor of Advanced Computing (R&D) (Honours)'), ('BADAN', 'Bachelor of Applied Data Analytics'), ('HADAN', 'Bachelor of Applied Data Analytics (Honours)'), ('BBIOT', 'Bachelor of Biotechnology'), ('HBIOT', 'Bachelor of Biotechnology (Honours)'), ('AENGI', 'Bachelor of Engineering (Honours)'), ('AENRD', 'Bachelor of Engineering (R&D) (Honours)'), ('BENSU', 'Bachelor of Environment and Sustainability'), ('HENSU', 'Bachelor of Environment and Sustainability (Honours)'), ('AENSU', 'Bachelor of Environment and Sustainability Advanced (Honours)'), ('HENVS', 'Bachelor of Environemntal Studies'), ('BGENE', 'Bachelor of Genetics'), ('HGENE', 'Bachelor of Genetics (Honours)'), ('BHLTH', 'Bachelor of Health Science (Honours)'), ('BIT', 'Bachelor of Information Technology'), ('HIT', 'Bachelor of Information Technology (Honours)'), ('BMASC', 'Bachelor of Mathematical Sciences'), ('HMASC', 'Bachelor of Mathematical Sciences (Honours)'), ('BMEDS', 'Bachelor of Medical Science'), ('HMEDS/HMDSA', 'Bachelor of Medical Science (Honours)'), ('PHBSCIENCE', 'PhB/Bachelor of Philosophy (Honours) in Science'), ('APSYC', 'Bachelor of Psychology (Honours)'), ('BSC', 'Science'), ('HSC', 'Bachelor of Science (Honours)'), ('ASCAD', 'Bachelor of Science (Advanced) (Honours)'), ('BSPSY', 'Science (Psychology)'), ('HSPSY', 'Bachelor of Science (Psychology) (Honours)'), ('ASENG', 'Bachelor of Software Engineering (Honours)'), ('ESCIE', 'Diploma of Science'), ('ECOMP', 'Diploma of Computing'), ('PHD', 'PhD/Doctor of Philosophy'), ('GDCP', 'Graduate Diploma of Computing'), ('MCOMP', 'Master of Computing'), ('VCOMP', 'Master of Computing (Advanced)'), ('MADAN', 'Master of Applied Data Analytics'), ('NDSTE', 'Master of Engineering in Digital Systems and Telecommunications'), ('NMECH', 'Master of Engineering in Mechatronics'), ('NENPH', 'Master of Engineering in Photonics'), ('NENRE', 'Master of Engineering in Renewable Energy'), ('MHCD', 'Doctor of Medicine and Surgery'), ('CSCIE', 'Graduate Certificate of Science'), ('DENVI', 'Graduate Diploma of Environment'), ('GDSCI', 'Graduate Diploma of Science'), ('VASTP', 'Master of Astronomy and Astrophysics (Advanced)'), ('MBIOS', 'Master of Biological Sciences'), ('VBIOS', 'Master of Biological Sciences (Advanced)'), ('MBIOT', 'Master of Biotechnology'), ('VBIOT', 'Master of Biotechnology (Advanced)'), ('MCPSY', 'Master of Clinical Psychology'), ('VEASC', 'Master of Earth Sciences (Advanced)'), ('MENCH', 'Master of Energy Change'), ('VENCH', 'Master of Energy Change (Advanced)'), ('MENVI', 'Master of Environment'), ('VENVI', 'Master of Environment (Advanced)'), ('MENVS', 'Master of Environemntal Science'), ('VENVS', 'Master of Environemntal Science (Advanced)'), ('MFORE', 'Master of Forestry'), ('VFORE', 'Master of Forestry (Advanced)'), ('VMASC', 'Master of Mathematical Sciences (Advanced)'), ('MNEUR', 'Master of Neuroscience'), ('VNEUR', 'Master of Neuroscience (Advanced)'), ('MNUCL', 'Master of Nuclear Science'), ('MPUBH', 'Master of Public Health'), ('VPUBH', 'Master of Public Health (Advanced)'), ('MSCHK', 'Master of Science Communication'), ('MSCO', 'Master of Science Communication Outreach'), ('MSCAU', 'Master of Science in Science Communication')], max_length=50, null=True),
        ),
    ]
