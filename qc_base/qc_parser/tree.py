import os
import os.path
import sys



# **File tree utility**
# 
# **Author:**  Darrell O. Ricke, Ph.D.  (mailto: Darrell.Ricke@ll.mit.edu)
#  Copyright:  Copyright (c) 2023 Massachusetts Institute of Technology 
#  License:    GNU GPL license (http://www.gnu.org/licenses/gpl.html)  
# 
# **RAMS request ID 1021178**
# 
# **Overview:**
# File tree utility
# 
# **Citation:** None
# 
# **Disclaimer:**
# DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.
# 
# This material is based upon work supported by the Defense Advanced Research 
# Projects Agency under Air Force Contract No. (FA8702- 15-D-0001). Any opinions, 
# findings and conclusions or recommendations expressed in this material are 
# those of the author(s) and do not necessarily reflect the views of the 
# Defense Advanced Research Projects Agency.
# 
# © 2023 Massachusetts Institute of Technology
# 
# The software/firmware is provided to you on an As-Is basis
# 
# Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS
# Part 252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice,
# U.S. Government rights in this work are defined by DFARS 252.227-7013 or
# DFARS 252.227-7014 as detailed above. Use of this work other than as specifically
# authorized by the U.S. Government may violate any copyrights that exist in this work.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


def samples( files ):

list = {}
  for f in files:
    i = f.find('_S')
    if i != -1:
      prefix = f[0:i]
      list[prefix] = prefix
  return list

namedir = sys.argv[1]

print('fastqs,sample,library_type')

gex_path = '/io/fastqs_gex/' + namedir + '/'
if os.path.isdir(gex_path):
  gex = os.listdir(gex_path)
  gex_samples = samples(gex)
  # print('GEX', gex_samples)
  for key in gex_samples:
    line = "/io/fastqs_gex/" + namedir + "," + key + ",Gene Expression"
    print(line)

atac_path = '/io/fastqs_atac/' + namedir
if os.path.isdir(atac_path):
  atac = os.listdir(atac_path)
  atac_samples = samples(atac)
  # print('ATAC:', atac_samples)
  for key in atac_samples:
    line = "/io/fastqs_atac/" + namedir + "," + key + ",Chromatin Accessibility"
    print(line)
