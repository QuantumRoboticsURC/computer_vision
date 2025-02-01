// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_interfaces:msg/CA.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__CA__STRUCT_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__CA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__custom_interfaces__msg__CA __attribute__((deprecated))
#else
# define DEPRECATED__custom_interfaces__msg__CA __declspec(deprecated)
#endif

namespace custom_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CA_
{
  using Type = CA_<ContainerAllocator>;

  explicit CA_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
      this->distance = 0.0;
      this->detected = false;
    }
  }

  explicit CA_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
      this->distance = 0.0;
      this->detected = false;
    }
  }

  // field types and members
  using _x_type =
    int32_t;
  _x_type x;
  using _distance_type =
    double;
  _distance_type distance;
  using _detected_type =
    bool;
  _detected_type detected;

  // setters for named parameter idiom
  Type & set__x(
    const int32_t & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__distance(
    const double & _arg)
  {
    this->distance = _arg;
    return *this;
  }
  Type & set__detected(
    const bool & _arg)
  {
    this->detected = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_interfaces::msg::CA_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_interfaces::msg::CA_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_interfaces::msg::CA_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_interfaces::msg::CA_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_interfaces::msg::CA_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_interfaces::msg::CA_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_interfaces::msg::CA_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_interfaces::msg::CA_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_interfaces::msg::CA_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_interfaces::msg::CA_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_interfaces__msg__CA
    std::shared_ptr<custom_interfaces::msg::CA_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_interfaces__msg__CA
    std::shared_ptr<custom_interfaces::msg::CA_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CA_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    if (this->detected != other.detected) {
      return false;
    }
    return true;
  }
  bool operator!=(const CA_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CA_

// alias to use template instance with default allocator
using CA =
  custom_interfaces::msg::CA_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__CA__STRUCT_HPP_
