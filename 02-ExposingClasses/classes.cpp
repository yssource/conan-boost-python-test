#include <boost/python.hpp>
#include <boost/python/extract.hpp>
#include <boost/python/list.hpp>
#include <sstream>
#include <string>
#include <vector>

struct World {
  void set(std::string msg) { mMsg = msg; }
  void many(boost::python::list msgs) {
    long l = len(msgs);
    std::stringstream ss;
    for (long i = 0; i < l; ++i) {
      if (i > 0)
        ss << ", ";
      std::string s = boost::python::extract<std::string>(msgs[i]);
      ss << s;
    }
    mMsg = ss.str();
  }
  std::string greet() { return mMsg; }
  std::string mMsg;
};

using namespace boost::python;

BOOST_PYTHON_MODULE(libclasses) {
  class_<World>("World")
      .def("greet", &World::greet)
      .def("set", &World::set)
      .def("many", &World::many);
};
