// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/CA.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__CA__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__CA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/msg/detail/ca__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_CA_detected
{
public:
  explicit Init_CA_detected(::custom_interfaces::msg::CA & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::CA detected(::custom_interfaces::msg::CA::_detected_type arg)
  {
    msg_.detected = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::CA msg_;
};

class Init_CA_distance
{
public:
  explicit Init_CA_distance(::custom_interfaces::msg::CA & msg)
  : msg_(msg)
  {}
  Init_CA_detected distance(::custom_interfaces::msg::CA::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_CA_detected(msg_);
  }

private:
  ::custom_interfaces::msg::CA msg_;
};

class Init_CA_x
{
public:
  Init_CA_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CA_distance x(::custom_interfaces::msg::CA::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_CA_distance(msg_);
  }

private:
  ::custom_interfaces::msg::CA msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::CA>()
{
  return custom_interfaces::msg::builder::Init_CA_x();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__CA__BUILDER_HPP_
