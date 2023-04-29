cmake_minimum_required(VERSION 3.15)
project(boost_test CXX)

find_package(Boost REQUIRED)

add_executable(boost_test src/boost_test.cpp src/main.cpp)
target_include_directories(boost_test PUBLIC include)

# target_link_libraries(${target}
#     PUBLIC
#     boost
# )

install(TARGETS boost_test)
