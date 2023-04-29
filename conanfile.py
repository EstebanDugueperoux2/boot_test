from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout
from conan.tools.build import cross_building

class BoostTestConan(ConanFile):
    name = "boost_test"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of BoostTest here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "test": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "test": False,
        "boost:without_stacktrace": True
    }

    def requirements(self):
        self.requires('boost/1.81.0')

    def build_requirements(self):
        self.tool_requires("cmake/3.25.3")
        self.tool_requires("ninja/1.11.1")
        # self.tool_requires("ccache/4.7.4")
        if self.options.test:
            self.test_requires("gtest/1.13.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        cmake = CMakeDeps(self)
        cmake.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
