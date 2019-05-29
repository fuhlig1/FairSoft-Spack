from spack import *
#import platform
#import compiler


class Fairroot(CMakePackage):
    """C++ simulation, reconstruction and analysis framework for particle physics experiments """


    homepage = "http://fairroot.gsi.de"
    url      = "https://github.com/FairRootGroup/FairRoot/archive/v18.0.6.tar.gz"

    # Development versions
    version('18.0.6', '822902c2fc879eab82fca47eccb14259')

    # Add all dependencies here.
    depends_on('cmake@3.11.1 +ownlibs', type='build')
    depends_on('googletest@1.7.0:')
    depends_on('boost@1.67.0 cxxstd=11')
    
    depends_on('pythia6@428-alice1')
    depends_on('pythia8@8212')

    depends_on('geant4@10.04.p01 cxxstd=11 ~qt~vecgeom~opengl~x11~motif+threads+data')

    # mesa and libxml2 are dependencies of root which have to be build extra due to the
    # extra build options
    depends_on('mesa~llvm')
    depends_on('libxml2+python')
    depends_on('root@6.12.06 cxxstd=11 +fortran+gdml+http+memstat+pythia6+pythia8+vc+xrootd+python~vdt')
    
    depends_on('geant3@v2-5-gcc8')
    depends_on('vgm@4-4')
    depends_on('geant4_vmc@3-6')

    depends_on('fairlogger@1.2.0')
    depends_on('fairmq@1.2.3')

#    depends_on('protobuf@3.4.0')
#    depends_on('flatbuffers@1.9.0')    
#    depends_on('millepede')       

    patch('CMake.patch', level=0)

    def setup_environment(self, spack_env, run_env):
        spack_env.append_flags('CXXFLAGS', '-std=c++11')

    def cmake_args(self):
        spec = self.spec
        options = []
        options.append('-DROOTSYS={0}'.format(
        self.spec['root'].prefix))
        options.append('-DROOT_CONFIG_SEARCHPATH={0}'.format(
        self.spec['root'].prefix))
#        options.append('-D={0}'.format(
#        self.spec[''].prefix))
        options.append('-DPythia6_LIBRARY_DIR={0}/lib'.format(
        self.spec['pythia6'].prefix))
        options.append('-DGeant3_DIR={0}'.format(
        self.spec['geant3'].prefix))
        options.append('-DGeant4_DIR={0}'.format(
        self.spec['geant4'].prefix))
        options.append('-DBOOST_ROOT={0}'.format(
        self.spec['boost'].prefix))
        options.append('-DBOOST_INCLUDEDIR={0}/include'.format(
        self.spec['boost'].prefix))
        options.append('-DBOOST_LIBRARYDIR={0}/lib'.format(
        self.spec['boost'].prefix))                                        
        options.append('-DDISABLE_GO=ON')
        options.append('-DBUILD_EXAMPLES=OFF')
        options.append('-DFAIRROOT_MODULAR_BUILD=ON')
        options.append('-DBoost_NO_SYSTEM_PATHS=TRUE')        
        options.append('-DCMAKE_EXPORT_COMPILE_COMMANDS=ON')

        return options
        
#        ${DDS_ROOT:+-DDDS_PATH=$DDS_ROOT}                                                     \                                                     
#        ${GSL_ROOT:+-DGSL_DIR=$GSL_ROOT}                                                      \
#        ${PROTOBUF_ROOT:+-DProtobuf_LIBRARY=$PROTOBUF_ROOT/lib/libprotobuf.$SONAME}           \
#        ${PROTOBUF_ROOT:+-DProtobuf_LITE_LIBRARY=$PROTOBUF_ROOT/lib/libprotobuf-lite.$SONAME} \
#        ${PROTOBUF_ROOT:+-DProtobuf_PROTOC_LIBRARY=$PROTOBUF_ROOT/lib/libprotoc.$SONAME}      \
#        ${PROTOBUF_ROOT:+-DProtobuf_INCLUDE_DIR=$PROTOBUF_ROOT/include}                       \
#        ${PROTOBUF_ROOT:+-DProtobuf_PROTOC_EXECUTABLE=$PROTOBUF_ROOT/bin/protoc}              \
#        ${CXXSTD:+-DCMAKE_CXX_STANDARD=$CXXSTD}                                               \

#    def install(self, spec, prefix):
#        # touch a file in the installation directory
#        touch('%s/this-is-a-bundle.txt' % prefix)

