##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import platform
import compiler
#import os
#import sys


class Fairsoft(Package):
    """Meta package to install all dependencies which are needed to properly install 
       and run FairRoot. No url or homepage is defined, only all packages whcih are
       needed are defined as dependencies. """


    homepage = ""
    url      = "https://github.com/fuhlig1/fairsoft_description/archive/17.10.tar.gz"

    # Development versions
    version('may18', '07e4938113b8a520a1d5dc67e7fbce50')

    # Add all dependencies here.
    depends_on('cmake', type='build')
    depends_on('googletest')
    depends_on('boost cxxstd=11')
    
    depends_on('pythia6')
    depends_on('pythia8')

    depends_on('geant4')

    depends_on('root')
    
    depends_on('geant3')
    depends_on('vgm')
    depends_on('geant4_vmc')

    depends_on('zeromq')
    depends_on('protobuf')
    depends_on('flatbuffers')
    depends_on('msgpack-c')

#    depends_on('millepede')       

    depends_on('fairlogger')
    def install(self, spec, prefix):
        # touch a file in the installation directory
        touch('%s/this-is-a-bundle.txt' % prefix)

