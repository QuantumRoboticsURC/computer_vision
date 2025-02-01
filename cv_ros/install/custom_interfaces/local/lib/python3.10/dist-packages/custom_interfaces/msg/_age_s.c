// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from custom_interfaces:msg/Age.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "custom_interfaces/msg/detail/age__struct.h"
#include "custom_interfaces/msg/detail/age__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool custom_interfaces__msg__age__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[31];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("custom_interfaces.msg._age.Age", full_classname_dest, 30) == 0);
  }
  custom_interfaces__msg__Age * ros_message = _ros_message;
  {  // years
    PyObject * field = PyObject_GetAttrString(_pymsg, "years");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->years = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // months
    PyObject * field = PyObject_GetAttrString(_pymsg, "months");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->months = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // days
    PyObject * field = PyObject_GetAttrString(_pymsg, "days");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->days = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * custom_interfaces__msg__age__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Age */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("custom_interfaces.msg._age");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Age");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  custom_interfaces__msg__Age * ros_message = (custom_interfaces__msg__Age *)raw_ros_message;
  {  // years
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->years);
    {
      int rc = PyObject_SetAttrString(_pymessage, "years", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // months
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->months);
    {
      int rc = PyObject_SetAttrString(_pymessage, "months", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // days
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->days);
    {
      int rc = PyObject_SetAttrString(_pymessage, "days", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
