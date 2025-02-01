// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_interfaces:msg/Coordinates.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__COORDINATES__STRUCT_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__COORDINATES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__custom_interfaces__msg__Coordinates __attribute__((deprecated))
#else
# define DEPRECATED__custom_interfaces__msg__Coordinates __declspec(deprecated)
#endif

namespace custom_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Coordinates_
{
  using Type = Coordinates_<ContainerAllocator>;

  explicit Coordinates_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude = 0.0;
      this->longitude = 0.0;
    }
  }

  explicit Coordinates_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude = 0.0;
      this->longitude = 0.0;
    }
  }

  // field types and members
  using _latitude_type =
    double;
  _latitude_type latitude;
  using _longitude_type =
    double;
  _longitude_type longitude;

  // setters for named parameter idiom
  Type & set__latitude(
    const double & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__longitude(
    const double & _arg)
  {
    this->longitude = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_interfaces::msg::Coordinates_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_interfaces::msg::Coordinates_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_interfaces::msg::Coordinates_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_interfaces::msg::Coordinates_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_interfaces__msg__Coordinates
    std::shared_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_interfaces__msg__Coordinates
    std::shared_ptr<custom_interfaces::msg::Coordinates_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Coordinates_ & other) const
  {
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    return true;
  }
  bool operator!=(const Coordinates_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Coordinates_

// alias to use template instance with default allocator
using Coordinates =
  custom_interfaces::msg::Coordinates_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__COORDINATES__STRUCT_HPP_
